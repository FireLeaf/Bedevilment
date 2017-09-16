/*******************************************************************
  FILE: Context.h
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: 场景上下文
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

#include "entityx/entityx.h"

namespace ex = entityx;

class FFMapComponent;

class FFContext : public ex::EntityX
{
public:
	FFContext();
	virtual ~FFContext();
public:
	virtual bool OnInitContext();
	virtual void OnSimulateContext(int timeDelta);
	virtual void OnDestroyContext();

	//virtual void StartContext();
	//virtual void JumpContext();
private:
	bool ConfigureContext();
private:
	FFMapComponent*		_MapComponent;	// 单例
};