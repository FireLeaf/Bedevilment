/******************************************************************************      
 *      Extended Mirror: SpecialMembers.cpp                                   *
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
#include <XM/Exceptions/NotFoundException.hpp>
#include <XM/Exceptions/MemberExceptions.hpp>

using namespace xm;

Constructor::Constructor(const Class& owner)
    : Item("", owner), Member("", owner) {};


void Constructor::init(Variant& var) const
{
    (void)(var);
    throw NonInstantiableException(getOwner());
}


CopyConstructor::CopyConstructor(const Class& owner)
    : Item("", owner), Member("", owner) {};


void CopyConstructor::copy(Variant& copy, const Variant& orig) const
{
    (void)(copy);
    (void)(orig);
    throw NonCopyableException(getOwner());
}


Destructor::Destructor(const Class& owner)
    : Item("", owner), Member("", owner) {};


void Destructor::destroy(Variant& var) const
{
    (void)(var);
    throw NonDestructibleException(getOwner());
}


RefCaster::RefCaster(const Class& dstClass, const Class& owner)
    : Item("", owner), dstClass_(&dstClass)
{
    if(owner.inheritsFrom(dstClass))
        castDir_ = UpCast;
    else if(dstClass.inheritsFrom(owner))
        castDir_ = DownCast;
    else
        castDir_ = NoCast;
}


CastDirection RefCaster::getCastDirection() const
{
    return castDir_;
}


const Class& RefCaster::getDstClass() const
{
    return *dstClass_;
}


Variant RefCaster::cast(const Variant& var) const
{
    (void) var;
    return Variant::Void;
}
