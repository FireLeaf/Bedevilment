/*******************************************************************
  FILE: Context.cpp
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: 
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#include "Context.h"
#include "Component/Transform.h"
#include "StateScript/StateScriptBase.h"
#include "Component/StateScript.h"
#include "System/StateScriptSystem.h"

FFContext::FFContext()
{
	const xm::Class& clazz = xm::getClass<FFTransformComponent>();
	clazz.getName();
}

FFContext::~FFContext()
{

}

bool FFContext::OnInitContext()
{
	if (!ConfigureContext())
	{
		return false;
	}

	return true;
}

bool FFContext::ConfigureContext()
{
	systems.add<FFStateScriptSystem>();
	systems.configure();

	return true;
}

void FFContext::OnSimulateContext(int timeDelta)
{
	systems.update_all(timeDelta);
}

void FFContext::OnDestroyContext()
{

}