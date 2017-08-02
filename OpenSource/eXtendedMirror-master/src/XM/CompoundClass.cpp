/******************************************************************************      
 *      Extended Mirror: CompoundClass.cpp                                    *
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


#include <XM/xMirror.hpp>

using namespace xm;
using namespace std;


CompoundClass::CompoundClass(const std::string& name,
                             const Namespace& name_space)
    : Item(name, name_space), Class(name, name_space)
{}


CompoundClass::CompoundClass
(
    const Namespace& name_space,
    const string& name,
    uint size,
    const type_info& cppType,
    const Constructor& constructor,
    const CopyConstructor& copyConstructor,
    const Destructor& destructor,
    bool isAbstract,
    const Template& tempjate
) :
    Item(name, name_space),
    Class
    (
        name_space,
        name,
        size,
        cppType,
        constructor,
        copyConstructor,
        destructor,
        isAbstract
    ),
    tempjate_(&tempjate)
{
}


void CompoundClass::addTemplateArg(const TemplArg& arg)
{
    templateArgs_.push_back(arg);
}


void CompoundClass::setTemplateArgs(const TemplArg_Vector& templateArgs)
{
    templateArgs_ = templateArgs;
}


Type::Category CompoundClass::getCategory() const
{
    return Type::CompoundClass;
}


const Template& CompoundClass::getTemplate() const
{
    return *tempjate_;
}


const TemplArg_Vector& CompoundClass::getTemplateArgs() const
{
    return templateArgs_;
}
