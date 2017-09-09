/******************************************************************************      
 *      Extended Mirror: RegistrationHelpers.hpp                              *
 ******************************************************************************
 *      Copyright (c) 2012-2015, Manuele Finocchiaro                          *
 *      All rights reserved.                                                  *
 ******************************************************************************
 * Redistribution and use in source and binary forms, with or without         *
 * modification, are permitted provided that the following conditions         *
 * are met:                                                                   *
 *                                                                            *
 *    1. Redistributions of source code must retain the above copyright       *
 *       notice, this list of conditions and the following disclaimer.        *
 *                                                                            *
 *    2. Redistributions in binary form must reproduce the above copyright    *
 *       notice, this list of conditions and the following disclaimer in      *
 *       the documentation and/or other materials provided with the           *
 *       distribution.                                                        *
 *                                                                            *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"* 
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE  *
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE *
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE  *
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR        *
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF       *
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS   *
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN    *
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)    *
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF     *
 * THE POSSIBILITY OF SUCH DAMAGE.                                            *
 *****************************************************************************/


#ifndef XM_REGISTRATIONHELPERS_HPP
#define	XM_REGISTRATIONHELPERS_HPP

#include <XM/Exceptions/NotFoundException.hpp>
#include <XM/Utils/Names.hpp>
#include "TypeTraits.hpp"


namespace xm {
    
template<typename T>
struct GetTypeName
{};


/**
 * The getSizeSignature method returns a string in the form [size_1][size_2]...[size_n]
 * if type T is an array in the form T[size_1][size_2]...[size_n],
 * an empty string if T is not an array.
 */
template<typename T>
struct GetArrayExtentsSignature
{
    std::string operator()()
    {
        return "";
    }
};


template<typename T, std::size_t size>
struct GetArrayExtentsSignature<T[size]>
{
    std::string operator()()
    {
        std::stringstream sstream;
        sstream << "[" << size << "]" << GetArrayExtentsSignature<T>()();
        return sstream.str();
    }
};


template<typename T, uint size>
struct GetTypeName<T[size]>
{
    typedef typename RemoveAllExtents<T>::Type NonArrayT;
    
    /**
     * If GetTypeName<T>::getName() returns "SomeType" then this method
     * returns "SomeType[size_1][size_2]...[size_n]".
     * 
     * @return The type name.
     */
    std::string operator()()
    {
        return GetTypeName<NonArrayT>()() +
                GetArrayExtentsSignature<T[size]>()();
    }
};


template<typename T>
struct GetTemplateName {};


template<typename T>
struct GetTemplateArgs {};


template<>
struct GetTypeName<void>
{
    std::string operator()()
    {
        return "void";
    }
};


template<typename T>
struct GetTypeName<T*>
{
    std::string operator()()
    {
        std::string str = GetTypeName<T>()();
        str += "*";
        return str;
    }
};


template<typename T, std::size_t size>
struct GetTypeName<T(*)[size]>
{
    std::string operator()()
    {
        std::string str = GetTypeName<T>()();
        str += "(*)";
        str += GetArrayExtentsSignature<T[size]>()();
        return str;
    }
};


template<typename T>
struct CreateType
{
    Type& operator()()
    {
        return *new PrimitiveType(GetTypeName<T>()(), sizeof(T), typeid(T));
    }
};


template<typename T>
struct CreateType<T*>
{
    Type& operator()()
    {
        const Type& pointedType = registerType<T>();
        
        return *new PointerType(GetTypeName<T*>()(), sizeof(T*), typeid(T*),
                pointedType);
    }
};


template<typename T, std::size_t size>
struct CreateType<T[size]>
{
    Type& operator()()
    {
        const Type& elementType = registerType<T>();
        
        return *new ArrayType(GetTypeName<T[size]>()(), sizeof(T[size]),
                typeid(T[size]), size, elementType);
    }
};


template<>
struct CreateType<void>
{
    Type& operator()()
    {
        return *new Class("void");
    }
};


template<class T>
struct IsAbstract : public FalseType {};


template<class T>
struct DefineClass
{
    void operator()(){}
};


/**
 * This helper function is called from the CreateType functor when registering
 * a class. This function is provided to keep the all the possible
 * code outside of macros.
 */

template<class T>
Class& createClass()
{
    // Get the typename
    std::string typeName = GetTypeName<T>()();

    // Split namespace from unqualified name
    std::pair<std::string, std::string> nameParts =
            splitName(typeName, NameTail);

    // Define namespace
    Namespace& name_space =
        Register::getSingleton().defineNamespace(nameParts.first);

    size_t templArgListPos = nameParts.second.find('<');

    if (templArgListPos == std::string::npos) {

        // Allocate memory for class
        Class* clazz = reinterpret_cast<Class*>(::operator new(sizeof(Class)));

        // Call constructor
        return *new (clazz) Class(name_space, nameParts.second, sizeof(T),
                typeid(T), *new ConstructorImpl<T>(*clazz),
                *new CopyConstructorImpl<T>(*clazz),
                *new DestructorImpl<T>(*clazz), IsAbstract<T>::value);
    } else {

        // Allocate memory for class
        CompoundClass* clazz = reinterpret_cast<CompoundClass*>(
                ::operator new(sizeof(CompoundClass)));

        // Get the template name
        const std::string tempjateName = typeName.substr(0, templArgListPos);

        // Get or create template
        const Template* tempjate;
        Register& typeReg = Register::getSingleton();
        try
        {
            tempjate = &typeReg.getItem<Template>(tempjateName);
        }
        catch(const NotFoundException& e)
        {
			(void)e;
            std::pair<std::string, std::string> nameParts
                    = splitName(tempjateName, NameTail);
            Namespace& name_space = xm::defineNamespace(nameParts.first);

            Template* ncTemplate = new Template(nameParts.second, name_space);

            typeReg.addItem(*ncTemplate);
            tempjate = ncTemplate;
        }

        return *new (clazz) CompoundClass(name_space, nameParts.second, sizeof(T),
                typeid(T), *new ConstructorImpl<T>(*clazz),
                *new CopyConstructorImpl<T>(*clazz), *new DestructorImpl<T>(*clazz),
                IsAbstract<T>::value, *tempjate);

    }
}


/**
 * This helper function is called from the CreateType functor when registering
 * a compound class. This function is provided to keep the all the possible
 * code outside of macros.
 */
template<class T>
CompoundClass& createCompoundClass()
{
    CompoundClass& clazz = dynamic_cast<CompoundClass&>(createClass<T>());

    clazz.setTemplateArgs(GetTemplateArgs<T>()());

    return clazz;
};


/**
 * This template class allow a class to be registered without any extra code
 * inside the main() or any other function.
 * Registration is performed by the constructor on instantiation.
 */
template<class T>
class TypeRegisterer
{
    TypeRegisterer()
    {
        registerType<T>();
    }
    
    static TypeRegisterer autoregisterer;
};

template<class T>
TypeRegisterer<T> TypeRegisterer<T>::autoregisterer;


} //namespace xm

#endif	/* XM_REGISTRATIONHELPERS_HPP */

