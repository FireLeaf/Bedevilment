/*******************************************************************
  FILE: StateScript.h
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: ×´Ì¬½Å±¾×é¼þ
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

#include "TypeDef.h"

class FFStateScript;

class FFStateScriptComponent
{
	std::list<FFStateScript*> ListStateScripts_;
};

XM_DECLARE_CLASS(FFStateScriptComponent)
XM_DEFINE_CLASS(FFStateScriptComponent)
{
	XM_BIND_VARIABLE("ListStateScripts_");
}

