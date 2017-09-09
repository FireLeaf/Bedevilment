/* WARNING: This file has been autogenerated. Do not modify it directly! */

#ifndef XM_BINDMETHOD_HPP
#define	XM_BINDMETHOD_HPP


namespace xm {



template
<
    class ClassT,
    typename RetT
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
    ) 
)
{
    // ensure the types are registered
    registerType<RetT>();
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_1_Params
        <
            ClassT,
            RetT
        >
        (
            uName,
            method,
            false
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
    ) const
)
{
    // ensure the types are registered
    registerType<RetT>();
    
    // remove the constness from the method
    RetT (ClassT::*method_nc)() =
        reinterpret_cast
        <
            RetT (ClassT::*)
            (
            )
        >(method);
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_1_Params
        <
            ClassT,
            RetT
        >
        (
            uName,
            method_nc,
            true
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1
    ) 
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_2_Params
        <
            ClassT,
            RetT,
            ParamT1
        >
        (
            uName,
            method,
            false
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1
    ) const
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    
    // remove the constness from the method
    RetT (ClassT::*method_nc)() =
        reinterpret_cast
        <
            RetT (ClassT::*)
            (
                ParamT1
            )
        >(method);
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_2_Params
        <
            ClassT,
            RetT,
            ParamT1
        >
        (
            uName,
            method_nc,
            true
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2
    ) 
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_3_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2
        >
        (
            uName,
            method,
            false
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2
    ) const
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    
    // remove the constness from the method
    RetT (ClassT::*method_nc)() =
        reinterpret_cast
        <
            RetT (ClassT::*)
            (
                ParamT1,
                ParamT2
            )
        >(method);
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_3_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2
        >
        (
            uName,
            method_nc,
            true
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3
    ) 
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_4_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3
        >
        (
            uName,
            method,
            false
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3
    ) const
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    
    // remove the constness from the method
    RetT (ClassT::*method_nc)() =
        reinterpret_cast
        <
            RetT (ClassT::*)
            (
                ParamT1,
                ParamT2,
                ParamT3
            )
        >(method);
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_4_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3
        >
        (
            uName,
            method_nc,
            true
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3,
    typename ParamT4
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3,
        ParamT4
    ) 
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    registerType<ParamT4>();
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_5_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3,
            ParamT4
        >
        (
            uName,
            method,
            false
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3,
    typename ParamT4
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3,
        ParamT4
    ) const
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    registerType<ParamT4>();
    
    // remove the constness from the method
    RetT (ClassT::*method_nc)() =
        reinterpret_cast
        <
            RetT (ClassT::*)
            (
                ParamT1,
                ParamT2,
                ParamT3,
                ParamT4
            )
        >(method);
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_5_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3,
            ParamT4
        >
        (
            uName,
            method_nc,
            true
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3,
    typename ParamT4,
    typename ParamT5
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3,
        ParamT4,
        ParamT5
    ) 
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    registerType<ParamT4>();
    registerType<ParamT5>();
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_6_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3,
            ParamT4,
            ParamT5
        >
        (
            uName,
            method,
            false
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3,
    typename ParamT4,
    typename ParamT5
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3,
        ParamT4,
        ParamT5
    ) const
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    registerType<ParamT4>();
    registerType<ParamT5>();
    
    // remove the constness from the method
    RetT (ClassT::*method_nc)() =
        reinterpret_cast
        <
            RetT (ClassT::*)
            (
                ParamT1,
                ParamT2,
                ParamT3,
                ParamT4,
                ParamT5
            )
        >(method);
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_6_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3,
            ParamT4,
            ParamT5
        >
        (
            uName,
            method_nc,
            true
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3,
    typename ParamT4,
    typename ParamT5,
    typename ParamT6
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3,
        ParamT4,
        ParamT5,
        ParamT6
    ) 
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    registerType<ParamT4>();
    registerType<ParamT5>();
    registerType<ParamT6>();
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_7_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3,
            ParamT4,
            ParamT5,
            ParamT6
        >
        (
            uName,
            method,
            false
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3,
    typename ParamT4,
    typename ParamT5,
    typename ParamT6
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3,
        ParamT4,
        ParamT5,
        ParamT6
    ) const
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    registerType<ParamT4>();
    registerType<ParamT5>();
    registerType<ParamT6>();
    
    // remove the constness from the method
    RetT (ClassT::*method_nc)() =
        reinterpret_cast
        <
            RetT (ClassT::*)
            (
                ParamT1,
                ParamT2,
                ParamT3,
                ParamT4,
                ParamT5,
                ParamT6
            )
        >(method);
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_7_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3,
            ParamT4,
            ParamT5,
            ParamT6
        >
        (
            uName,
            method_nc,
            true
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3,
    typename ParamT4,
    typename ParamT5,
    typename ParamT6,
    typename ParamT7
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3,
        ParamT4,
        ParamT5,
        ParamT6,
        ParamT7
    ) 
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    registerType<ParamT4>();
    registerType<ParamT5>();
    registerType<ParamT6>();
    registerType<ParamT7>();
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_8_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3,
            ParamT4,
            ParamT5,
            ParamT6,
            ParamT7
        >
        (
            uName,
            method,
            false
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



template
<
    class ClassT,
    typename RetT,
    typename ParamT1,
    typename ParamT2,
    typename ParamT3,
    typename ParamT4,
    typename ParamT5,
    typename ParamT6,
    typename ParamT7
>
Method& bindMethod
(
    const std::string& uName,
    RetT (ClassT::*method)
    ( 
        ParamT1,
        ParamT2,
        ParamT3,
        ParamT4,
        ParamT5,
        ParamT6,
        ParamT7
    ) const
)
{
    // ensure the types are registered
    registerType<RetT>();
    registerType<ParamT1>();
    registerType<ParamT2>();
    registerType<ParamT3>();
    registerType<ParamT4>();
    registerType<ParamT5>();
    registerType<ParamT6>();
    registerType<ParamT7>();
    
    // remove the constness from the method
    RetT (ClassT::*method_nc)() =
        reinterpret_cast
        <
            RetT (ClassT::*)
            (
                ParamT1,
                ParamT2,
                ParamT3,
                ParamT4,
                ParamT5,
                ParamT6,
                ParamT7
            )
        >(method);
    
    // create the proper Method
    Method* xmMethod = new MethodImpl_8_Params
        <
            ClassT,
            RetT,
            ParamT1,
            ParamT2,
            ParamT3,
            ParamT4,
            ParamT5,
            ParamT6,
            ParamT7
        >
        (
            uName,
            method_nc,
            true
        );

    const_cast<Class&>(getClass<ClassT>()).addMember(*xmMethod);
    return *xmMethod;
}



} // namespace xm

#endif	/* XM_BINDMETHOD_HPP */