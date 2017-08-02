/* WARNING: This file has been autogenerated. Do not modify it directly! */

#include <XM/xMirror.hpp>

using namespace std;
using namespace xm;

Variant Variant::call
(
    const std::string& methodName,
    const Variant& arg0,
    const Variant& arg1,
    const Variant& arg2,
    const Variant& arg3,
    const Variant& arg4,
    const Variant& arg5,
    const Variant& arg6
)
{   
    const Class* clazz = dynamic_cast<const Class*>(type_);
    if (clazz)
    {
        Method keyMethod
        (
            methodName,
            xm::getType<void>(),
            *clazz,
            arg0.getType(),
            arg1.getType(),
            arg2.getType(),
            arg3.getType(),
            arg4.getType(),
            arg5.getType(),
            arg6.getType()
        );
        const Method& callableMethod = clazz->getMethod(keyMethod);
        
        return callableMethod.call(
                                      *this,
                                      arg0,
                                      arg1,
                                      arg2,
                                      arg3,
                                      arg4,
                                      arg5,
                                      arg6
        );
    }
    else
    {
        // TODO: throw something appropriate
        throw 0;
    }
}


Variant Variant::callV(const std::string& methodName,
        vector<Variant>& args)
{
    args.resize(XM_FUNCTION_PARAM_MAX, Variant::Void);
    return call
    (
        methodName,
        args[0],
        args[1],
        args[2],
        args[3],
        args[4],
        args[5],
        args[6]
    );
}
