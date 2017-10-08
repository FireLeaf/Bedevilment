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
	FFVector3	_Position;		// λ��
	FFVector3	_Direction;		// ����
};

XM_DECLARE_CLASS(FFTransformComponent);
XM_DEFINE_CLASS(FFTransformComponent)
{
	bindProperty(XM_MNP(_Position));
	bindProperty(XM_MNP(_Direction));
}