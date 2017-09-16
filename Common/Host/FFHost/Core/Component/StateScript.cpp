/*******************************************************************************
FILE:		StateScript.cpp

DESCRIPTTION: 

CREATED BY: YangCao, 2017/09/10

Copyright (C) - All Rights Reserved with Coconat
*******************************************************************************/

#include "StateScript.h"
#include "StateScript/StateScriptBase.h"

XM_DEFINE_CLASS(std::list<FFStateScriptBase*>)
{
	XM_ADD_TEMPL_ARG(xm::getType<FFStateScriptBase*>());
}

XM_DEFINE_CLASS(FFStateScriptComponent)
{
	bindProperty(XM_MNP(_ListStateScripts));
}