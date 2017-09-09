/*******************************************************************
  FILE: Transform.h
 
  CREATED BY: YangCao , 2017.09.02
 
  HISTORY: 
 
  DESCRIPTION: λ�����
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

#include "TypeDef.h"

struct FFTransformComponent
{
	FFVector3	Position_;		// λ��
	FFVector3	Direction_;		// ����
};

XM_DECLARE_CLASS(FFTransformComponent);
XM_DEFINE_CLASS(FFTransformComponent)
{
	XM_BIND_VARIABLE("Position_");
	XM_BIND_VARIABLE("Direction_");
}