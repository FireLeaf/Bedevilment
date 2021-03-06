/* WARNING: This file has been autogenerated. Do not modify it directly! */

#ifndef XM_BINDTEMPLATE_HPP
#define XM_BINDTEMPLATE_HPP

#define XM_DECLARE_TEMPLATE_PARAM_MAX 4


/**
 * \def XM_DECLARE_TEMPLATE_1(_template_)
 * 
 * Use to enable instances of template class to be registered as such.
 * 
 * Works only with two type parameters template classes.
 * After this macro, specify the body of the building function.
 */
#define XM_DECLARE_TEMPLATE_1(_template_)       \
namespace xm{                                                                \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0                                \
>                                                                            \
struct GetTypeName                                                           \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    std::string operator()()                                                 \
    {                                                                        \
        std::string str = std::string(#_template_) + "<";                    \
        str += GetTypeName<T0>()();     \
        str += ">";                                                          \
        return str;                                                          \
    }                                                                        \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0                                \
>                                                                            \
struct GetTemplateArgs                                                       \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    TemplArg_Vector operator()()                                             \
    {                                                                        \
        TemplArg_Vector templateArgs;                                        \
        templateArgs.push_back(registerType<T0>()); \
        return templateArgs;                                                 \
    }                                                                        \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0                                \
>                                                                            \
struct DefineClass                                                           \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    typedef _template_                                                       \
    <                                                                        \
        T0                                     \
    > ClassT;                                                                \
    void operator()();                                                       \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0                                \
>                                                                            \
struct CreateType                                                            \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    Type& operator()()                                                       \
    {                                                                        \
        return createCompoundClass                                           \
            <                                                                \
                _template_                                                   \
                <                                                            \
                    T0                         \
                >                                                            \
            >();                                                             \
    }                                                                        \
};                                                                           \
                                                                             \
} // namespace xm



/**
 * \def XM_DECLARE_TEMPLATE_2(_template_)
 * 
 * Use to enable instances of template class to be registered as such.
 * 
 * Works only with two type parameters template classes.
 * After this macro, specify the body of the building function.
 */
#define XM_DECLARE_TEMPLATE_2(_template_)       \
namespace xm{                                                                \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1                                \
>                                                                            \
struct GetTypeName                                                           \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    std::string operator()()                                                 \
    {                                                                        \
        std::string str = std::string(#_template_) + "<";                    \
        str += GetTypeName<T0>()();                         \
        str += ", " + GetTypeName<T1>()();     \
        str += ">";                                                          \
        return str;                                                          \
    }                                                                        \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1                                \
>                                                                            \
struct GetTemplateArgs                                                       \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    TemplArg_Vector operator()()                                             \
    {                                                                        \
        TemplArg_Vector templateArgs;                                        \
        templateArgs.push_back(registerType<T0>());         \
        templateArgs.push_back(registerType<T1>()); \
        return templateArgs;                                                 \
    }                                                                        \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1                                \
>                                                                            \
struct DefineClass                                                           \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    typedef _template_                                                       \
    <                                                                        \
        T0,                                                 \
        T1                                     \
    > ClassT;                                                                \
    void operator()();                                                       \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1                                \
>                                                                            \
struct CreateType                                                            \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    Type& operator()()                                                       \
    {                                                                        \
        return createCompoundClass                                           \
            <                                                                \
                _template_                                                   \
                <                                                            \
                    T0,                                     \
                    T1                         \
                >                                                            \
            >();                                                             \
    }                                                                        \
};                                                                           \
                                                                             \
} // namespace xm



/**
 * \def XM_DECLARE_TEMPLATE_3(_template_)
 * 
 * Use to enable instances of template class to be registered as such.
 * 
 * Works only with two type parameters template classes.
 * After this macro, specify the body of the building function.
 */
#define XM_DECLARE_TEMPLATE_3(_template_)       \
namespace xm{                                                                \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1,                                            \
    typename T2                                \
>                                                                            \
struct GetTypeName                                                           \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    std::string operator()()                                                 \
    {                                                                        \
        std::string str = std::string(#_template_) + "<";                    \
        str += GetTypeName<T0>()();                         \
        str += ", " + GetTypeName<T1>()();                         \
        str += ", " + GetTypeName<T2>()();     \
        str += ">";                                                          \
        return str;                                                          \
    }                                                                        \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1,                                            \
    typename T2                                \
>                                                                            \
struct GetTemplateArgs                                                       \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    TemplArg_Vector operator()()                                             \
    {                                                                        \
        TemplArg_Vector templateArgs;                                        \
        templateArgs.push_back(registerType<T0>());         \
        templateArgs.push_back(registerType<T1>());         \
        templateArgs.push_back(registerType<T2>()); \
        return templateArgs;                                                 \
    }                                                                        \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1,                                            \
    typename T2                                \
>                                                                            \
struct DefineClass                                                           \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    typedef _template_                                                       \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2                                     \
    > ClassT;                                                                \
    void operator()();                                                       \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1,                                            \
    typename T2                                \
>                                                                            \
struct CreateType                                                            \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    Type& operator()()                                                       \
    {                                                                        \
        return createCompoundClass                                           \
            <                                                                \
                _template_                                                   \
                <                                                            \
                    T0,                                     \
                    T1,                                     \
                    T2                         \
                >                                                            \
            >();                                                             \
    }                                                                        \
};                                                                           \
                                                                             \
} // namespace xm



/**
 * \def XM_DECLARE_TEMPLATE_4(_template_)
 * 
 * Use to enable instances of template class to be registered as such.
 * 
 * Works only with two type parameters template classes.
 * After this macro, specify the body of the building function.
 */
#define XM_DECLARE_TEMPLATE_4(_template_)       \
namespace xm{                                                                \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1,                                            \
    typename T2,                                            \
    typename T3                                \
>                                                                            \
struct GetTypeName                                                           \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2,                                                 \
        T3                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    std::string operator()()                                                 \
    {                                                                        \
        std::string str = std::string(#_template_) + "<";                    \
        str += GetTypeName<T0>()();                         \
        str += ", " + GetTypeName<T1>()();                         \
        str += ", " + GetTypeName<T2>()();                         \
        str += ", " + GetTypeName<T3>()();     \
        str += ">";                                                          \
        return str;                                                          \
    }                                                                        \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1,                                            \
    typename T2,                                            \
    typename T3                                \
>                                                                            \
struct GetTemplateArgs                                                       \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2,                                                 \
        T3                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    TemplArg_Vector operator()()                                             \
    {                                                                        \
        TemplArg_Vector templateArgs;                                        \
        templateArgs.push_back(registerType<T0>());         \
        templateArgs.push_back(registerType<T1>());         \
        templateArgs.push_back(registerType<T2>());         \
        templateArgs.push_back(registerType<T3>()); \
        return templateArgs;                                                 \
    }                                                                        \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1,                                            \
    typename T2,                                            \
    typename T3                                \
>                                                                            \
struct DefineClass                                                           \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2,                                                 \
        T3                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    typedef _template_                                                       \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2,                                                 \
        T3                                     \
    > ClassT;                                                                \
    void operator()();                                                       \
};                                                                           \
                                                                             \
template                                                                     \
<                                                                            \
    typename T0,                                            \
    typename T1,                                            \
    typename T2,                                            \
    typename T3                                \
>                                                                            \
struct CreateType                                                            \
<                                                                            \
    _template_                                                               \
    <                                                                        \
        T0,                                                 \
        T1,                                                 \
        T2,                                                 \
        T3                                     \
    >                                                                        \
>                                                                            \
{                                                                            \
    Type& operator()()                                                       \
    {                                                                        \
        return createCompoundClass                                           \
            <                                                                \
                _template_                                                   \
                <                                                            \
                    T0,                                     \
                    T1,                                     \
                    T2,                                     \
                    T3                         \
                >                                                            \
            >();                                                             \
    }                                                                        \
};                                                                           \
                                                                             \
} // namespace xm



#endif	/* XM_BINDTEMPLATE_HPP */