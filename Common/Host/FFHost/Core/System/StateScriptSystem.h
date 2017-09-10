/*******************************************************************
  FILE: StateScriptSystem.h
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: ״̬�ű�ϵͳ
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
  *******************************************************************/

#pragma once

#include "entityx/entityx.h"

namespace ex = entityx;

class FFStateScriptSystem : ex::System<FFStateScriptSystem>
{
public:
	virtual void update(ex::EntityManager &es, ex::EventManager &events, ex::TimeDelta dt) override
	{
		es.each<FFStateScriptComponent>([] (ex::Entity entity, FFStateScriptComponent& component){
			for (auto stateScriptIter = component.ListStateScripts_.begin(); stateScriptIter != component.ListStateScripts_.end();)
			{
				stateScriptIter->OnSimulate(dt);
			}
		});
	}
};