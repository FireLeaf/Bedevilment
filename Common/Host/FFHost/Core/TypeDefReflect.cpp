/*******************************************************************************
FILE:		TypeDefReflect.cpp

DESCRIPTTION: 

CREATED BY: YangCao, 2017/09/10

Copyright (C) - All Rights Reserved with Coconat
*******************************************************************************/

#include "TypeDef.h"

XM_DEFINE_CLASS(v3d)
{
	bindProperty(XM_MNP(x));
	bindProperty(XM_MNP(y));
	bindProperty(XM_MNP(z));
}

XM_DEFINE_CLASS(v2d)
{
	bindProperty(XM_MNP(x));
	bindProperty(XM_MNP(y));
}