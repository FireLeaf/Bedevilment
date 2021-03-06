/*******************************************************************
  FILE: StateScript.h
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: ״̬�ű����
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

#include "TypeDef.h"

class FFStateScriptBase;

struct FFStateScriptComponent
{
	std::list<FFStateScriptBase*>		_ListStateScripts;
	std::vector<FFStateScriptBase*>		_DelayStateScripts;
	bool								_IsInProcessState;
};

XM_DECLARE_CLASS(std::list<FFStateScriptBase*>)
XM_DECLARE_CLASS(FFStateScriptComponent)
