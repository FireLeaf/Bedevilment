/*******************************************************************
  FILE: TypeDef.h
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: 类型重定义
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

#include <vector>
#include <list>
#include <map>
//#include <unordered_map>

#include "xm/xMirror.hpp"

#include "fix16.hpp"
#include "fixmatrix.h"
#include "fixquat.h"
#include "fixvector2d.h"
#include "fixvector3d.h"

/*
using FFFloat = fix16_t;
using FFMatrix = mf16;
using FFQuat = qf16;
using FFVector2 = v2d;
using FFVector3 = v3d;
*/
typedef fix16_t FFFloat;
typedef mf16 FFMatrix;
typedef qf16 FFQuat;
typedef v2d FFVector2;
typedef v3d FFVector3;

XM_DECLARE_CLASS(v3d)
XM_DECLARE_CLASS(v2d)