/******************************************************************************      
 *      Extended Mirror: Type.cpp                                             *
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

using namespace std;
using namespace xm;

Type::Type(const string& uName)
    : Item(uName), size_(0), id_(typeid(void))
{}


Type::Type(const string& uName, const Namespace& name_space)
    : Item(uName, name_space), size_(0), id_(typeid(void))
{}


Type::Type(const type_info& cppType)
    : size_(0), id_(cppType)
{}


Type::Type(size_t size, const type_info& cppType)
    : size_(size), id_(cppType)
{}


Type::Category Type::getCategory() const
{
    return static_cast<Type::Category>(0);
}


const String_Set& Type::getAliases() const
{
    return aliases_;
}


std::size_t Type::getSize() const
{
    return size_;
}


const type_info& Type::getId() const
{
    return id_;
}


bool Type::before(const Item& item) const
{
    if (dynamic_cast<const Member*>(&item))
        return true;
    return Item::before(item);
}


void Type::addAlias(const string& alias)
{
    aliases_.insert(alias);
}


Item::Category Type::getItemCategory() const
{
    return TypeItem;
}


Type::~Type()
{

}
