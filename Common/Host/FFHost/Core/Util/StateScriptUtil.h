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

class FFStateScriptSystem : public ex::System<FFStateScriptSystem>
{
public:
	virtual void update(ex::EntityManager &es, ex::EventManager &events, ex::TimeDelta dt) override
	{
		es.each<FFStateScriptComponent>([dt] (ex::Entity entity, FFStateScriptComponent& component){

			component._IsInProcessState = true;
			for (auto stateScriptIter = component._ListStateScripts.begin(); stateScriptIter != component._ListStateScripts.end();)
			{
				(*stateScriptIter)->OnSimulate(dt);
			}
			component._IsInProcessState = false;
			for (auto delayIter = component._DelayStateScripts.begin(); delayIter != component._DelayStateScripts.end(); delayIter++)
			{
				component._ListStateScripts.emplace_back(*delayIter);
			}
		});
	}
};