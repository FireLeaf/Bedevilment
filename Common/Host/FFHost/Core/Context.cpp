/*******************************************************************
  FILE: Context.cpp
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: 
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#include "Context.h"
#include "Component/Transform.h"
#include "Component/StateScript.h"

FFContext::FFContext()
{
	const xm::Class& clazz = xm::getClass<FFTransformComponent>();
	clazz.getName();
}

FFContext::~FFContext()
{

}