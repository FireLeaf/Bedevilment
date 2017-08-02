/******************************************************************************
 *      Extended Mirror: Register.cpp                                         *
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


#include <XM/Utils/Utils.hpp>
#include <XM/xMirror.hpp>
#include <XM/Exceptions/NotFoundException.hpp>


using namespace std;
using namespace xm;


Register& Register::getSingleton()
{
    static Register typeReg;
    return typeReg;
}


Register::Register()
{
}


const Type& Register::getType(const type_info& cppType) const
{
    const Type* type = ptrSet::findByKey(types_, cppType);
    if (type)
        return *type;
    else
        throw NotFoundException(cppType);
}


const Class& Register::getClass(const type_info& cppType) const
{
    return dynamic_cast<const Class&>(getType(cppType));
}


Register::~Register()
{

}

XM_REGISTER_TYPE(void)
XM_REGISTER_TYPE(bool)
XM_REGISTER_TYPE(char)
XM_REGISTER_TYPE(short)
XM_REGISTER_TYPE(int)
XM_REGISTER_TYPE(long)
XM_REGISTER_TYPE(float)
XM_REGISTER_TYPE(double)
XM_REGISTER_TYPE(uchar)
XM_REGISTER_TYPE(ushort)
XM_REGISTER_TYPE(uint)
XM_REGISTER_TYPE(ulong)
