/*******************************************************************
  FILE: Transform.h
 
  CREATED BY: YangCao , 2017.09.02
 
  HISTORY: 
 
  DESCRIPTION: 位置组件
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

#include "TypeDef.h"

struct FFTransformComponent
{
	FFVector3	Position_;		// 位置
	FFVector3	Direction_;		// 朝向
};

XM_DECLARE_CLASS(FFTransformComponent);
XM_DEFINE_CLASS(FFTransformComponent)
{
	XM_BIND_VARIABLE("Position_");
	XM_BIND_VARIABLE("Direction_");
}