/******************************************************************************      
 *      Extended Mirror: Class.hpp                                         *
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


#ifndef XM_CLASS_HPP
#define	XM_CLASS_HPP


namespace xm
{

typedef std::set<const RefCaster*, PtrCmpByVal<RefCaster> > Const_RefCaster_Set;
typedef std::set<const Class*, PtrCmpByName<Class> > Const_Class_Set;


class Class : public Type, public Namespace
{
public:
    
    /**
     * Basic constructor for initialization.
     * 
     * @param uName The unqualified class name.
     */
    Class(const std::string& uName = "");

    /**
     * Basic constructor for initialization.
     *
     * @param uName The unqualified class name.
     */
    Class(const std::string& uName, const Namespace& name_space);
    
    /**
     * Ask if the class is abstract.
     * 
     * @return True if the class is abstract, false otherwise.
     */
    bool isAbstract() const;
    
    /**
     * Get the constructor of the class.
     * 
     * @throws NonInstantiableException
     * @return The class constructor.
     */
    const Constructor& getConstructor() const;
    
    /**
     * Get the copy constructor of the class.
     * 
     * @throws NonCopyableException.
     * @return The class copy constructor.
     */
    const CopyConstructor& getCopyConstructor() const;
    
    /**
     * Get the destructor of the class.
     * 
     * @throws NonDestructibleException.
     * @return The class assign operator constructor.
     */
    const Destructor& getDestructor() const;
    
     /**
     * Retrieve all the base class descriptors.
     *
     * @param indirect If the indirect base classes should be included.
     *
     * @return A set containing the pointers to the base classes.
     */
    const Const_Class_Set& getBaseClasses(bool indirect = false) const;
    
    /**
     * Retrieve all the reference casters.
     * 
     * @return A set containing the pointers to the reference casters.
     */
    const Const_RefCaster_Set& getRefCasters() const;
    
    /**
     * Retrieve all the derived class descriptors.
     * 
     * @return A set containing the pointers to the derived Classes.
     */
    const Const_Class_Set& getDerivedClasses() const;
    
    /**
     * Retrieve all the property descriptors of this class. Note that the
     * properties inherited form the base classes are not included.
     * 
     * @param inherited Whether to include inherited properties.
     * @return A set containing the pointers to the class property objects.
     */
    const Const_Property_Set& getProperties(bool inherited = true) const;
    
    /**
     * Retrieve all the Methods of this class.
     * 
     * @param inherited Whether to include inherited methods.
     * @return A set containing the pointers to the class method objects.
     */
    const Const_Method_Set& getMethods(bool inherited = true) const;
    
    /**
     * Check whether or not the class has a Property with the given name.
     * 
     * @param propertyName The name of the Property.
     * @param inherited Whether to search through inherited properties too.
     * @return true if the class has the property, false otherwise.
     */
    bool hasProperty(const std::string& propertyName, bool inherited = true)
    const;
    
    /**
     * Check whether or not the class has a Method with the given name.
     * 
     * @param methodName The name of the method.
     * @param inherited Whether to search through inherited methods too.
     * @return true if the class has the method, false otherwise.
     */
    bool hasMethod(const std::string& methodName, bool inherited = true) const;
    
    /**
     * Check whether or not the class has a Method with the given signature.
     * 
     * @param method The Method with the given signature.
     * @param inherited Whether to search through inherited methods too.
     * @return true if the class has the method, false otherwise.
     */
    bool hasMethod(const Method& method, bool inherited = true) const;
    
    /**
     * Check whether or not the class inherits from a class with the given name.
     * 
     * @param baseClassName The name of the class.
     * @return true if the class derives from the given one, false otherwise.
     */
    bool inheritsFrom(const std::string& baseClassName) const;
    
    /**
     * Check whether or not the class derives from a given class.
     * 
     * @param baseClass The type of the derived class
     * @return true if the class derives from the given one, false otherwise. 
     */
    bool inheritsFrom(const Class& baseClass) const;
    
    /**
     * Get the Property with the given property name.
     * 
     * To see if there is a property with that name call first the hasProperty()
     * method.
     * 
     * @param propertyName The name of the property.
     * @return The Property with that name.
     */
    const Property& getProperty(const std::string& propertyName) const;
    
    /**
     * Get the Method of the method with the given name.
     * 
     * To see if there is a method with that name call first the hasMethod()
     * method.
     * If there are more than one overloaded methods registered with the same
     * name the first one according with the sorting rules will be returned.
     * To have more control over the overloaded methods use getMethod with the
     * whole signature information.
     * 
     * @param methodName The name of the method.
     * @return The Method of the method with this name.
     */
    const Method& getMethod(const std::string& methodName) const;
    
    /**
     * Get the Method of the method with the given signature.
     * 
     * To see if there is a method with that name call first the hasMethod()
     * method.
     * 
     * @param method The Method with the signature you want to retrieve.
     * 
     * @return The Method of the method with the specified signature.
     */
    const Method& getMethod(const Method& method) const;
    
    /**
     * Get the type Category.
     * 
     * @return The type category of this type.
     */
    Category getCategory() const;
    
    void addBaseClass(Class& baseClass);
    
    void addMember(Member& member);
    
    Item::Category getItemCategory() const;
    
    virtual ~Class();
    
protected:
    
    /**
     * Constructor for full initialization.
     * 
     * @param name_space The class name_space.
     * @param uName The unqualified class name.
     * @param size The class size.
     * @param cppType The type_info struct of the class.
     * @param constructor The class constructor wrapper function.
     * @param copyConstructor The type copy constructor wrapper function.
     * @param destructor The class destructor wrapper function.
     * @param isAbstract If the class is abstract.
     */
    Class
    (
            const Namespace& name_space,
            const std::string& uName,
            std::size_t size,
            const std::type_info& cppType,
            const Constructor& constructor,
            const CopyConstructor& copyConstructor,
            const Destructor& destructor,
            bool isAbstract
     );

    Namespace& walkTo(const std::string& path, bool create = false);
    
    const Constructor* constructor_;
    
    const CopyConstructor* copyConstructor_;
    
    const Destructor* destructor_;
    
    Const_Class_Set baseClasses_;

    Const_Class_Set indirectBaseClasses_;
    
    Const_RefCaster_Set refCasters_;

    Const_Class_Set derivedClasses_;

    // The properties of this class.
    Const_Property_Set properties_;
    
    // The properties of this class except those inherited from base classes.
    Const_Property_Set ownProperties_;
    
    // The methods of this class.
    Const_Method_Set methods_;
    
    // The methods of this class except those inherited form base classes.
    Const_Method_Set ownMethods_;
    
    bool isAbstract_;
    
    // Factory function
    template<class T>
    friend Class& createClass();
    
    // The DefineClass needs to call the & operator.
    template<class T>
    friend struct DefineClass;
};


bool inline operator<(const RefCaster& rc1, const RefCaster& rc2)
{
    return dynamic_cast<const Type&>(*rc1.dstClass_) <
        dynamic_cast<const Type&>(*rc2.dstClass_);
}


} // namespace xm
#endif	/* XM_CLASS_HPP */

