/******************************************************************************      
 *      Extended Mirror: Register.hpp                                         *
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


#ifndef XM_REGISTER_HPP
#define XM_REGISTER_HPP

namespace xm{

class Type;
class Class;
class CompoundClass;

typedef std::set<Type*, PtrCmpByVal<Type> > Type_SetByVal;
typedef std::set<Class*, PtrCmpByVal<Class> > Class_SetByVal;


class Register : public Namespace
{
public:
    
    const Type& getType(const std::type_info& cppType) const;
    
    const Class& getClass(const std::type_info& cppType) const;
    
    template<typename T>
    const Type& getTypeOf(const T& obj) const;
    
    template<typename T>
    const Class& getClassOf(const T& obj) const;
    
    template<typename T>
    const Type& getType() const;
    
    template<typename T>
    const Class& getClass() const;
    
    const Namespace& getRootNamespace() const;
    
    template<typename T>
    const Type& registerType();
    
    template<typename T>
    const Class& registerClass();
    
    void unregisterType(const std::string& typeName);
    
    void unregisterType(const std::type_info& cppType);
    
    /**
     * Set a function that is called whenever a type is registered within the
     * type register and the registered type is passed to this function.
     * 
     * @param callBackFnc
     */
    void setRegCallBack(void (*callBackFnc)(const Type&));
    
    static Register& getSingleton();
    
private:

     /*
      * Singleton restrictions.
      */
    Register();
    
    Register(const Register&);
    Register& operator=(const Register&);
    
    ~ Register();
    
    /**
     * This method is called by registerType, after the type qualifiers are
     * removed from the type.
     * 
     * @return the registered type.
     */
    template<typename T> Type& registerType_();
    
    /**
     * Return the function pointer of the callback function to call after each
     * type registration.
     * 
     * @return The callback function pointer.
     */
    static void (*getRegCallBack())(const Type&);
    
    // types and classes sets sorted by type id.
    Type_SetByVal types_;
    Class_SetByVal classes_;
    
    // this class needs to add Templates to the register
    friend class CompoundClass;
};


} // namespace xm

#endif // XM_REGISTER_HPP
