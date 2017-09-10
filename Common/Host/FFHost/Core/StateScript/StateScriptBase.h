/*******************************************************************
  FILE: StateScriptBase.h
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: ×´Ì¬½Å±¾»ùÀà
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
  *******************************************************************/

#pragma once

#include "TypeDef.h"
#include "lua.h"

#include <functional>

struct FFTimer
{
public:
	FFTimer(int peroid, bool isOnce, std::function<void()> timerHandler)
	{
		_Period = peroid;
		_IsOnce = isOnce;
		_TimerHandler = timerHandler;
		
		_CurDuration = 0;
		_IsFinish = false;
	}
public:
	void OnSimulate(int timeDelta)
	{
		_CurDuration += timeDelta;
		while (_CurDuration <= _Period)
		{
			_CurDuration -= _Period;
			_TimerHandler();

			if (_IsOnce)
			{
				_IsFinish = true;
				break;
			}
		}
	}

	void ResetTimer()
	{
		_CurDuration = 0;
	}

public:
	bool	IsOnce() const			{ return _IsOnce; }
	int		GetPeroid() const		{ return _Period; }
	int		GetCurDuration() const	{ return _CurDuration; }
	bool	IsFinish() const		{ return _IsFinish; }
private:
	int						_Period;
	bool					_IsOnce;
	int						_CurDuration;
	std::function<void()>	_TimerHandler;
	bool					_IsFinish;
};

class FFStateScriptBase
{
public:
	FFStateScriptBase() {}
	virtual ~FFStateScriptBase() {}
public:
	void AddStateTimer(int peroid, bool isOnce, std::function<void()> timerHandler) {
		FFTimer timer(peroid, isOnce, timerHandler);
		if (_IsSimTimer)
			_DelayTimers.emplace_back(timer);
		else
			_ListTimer.emplace_back(timer);
	}
public:
	virtual void OnCreate() {}
	virtual void OnActive() {}
	virtual void OnSimulate(int timeDelta) {
		SimulateTimer(timeDelta);
	}
	virtual void OnDeactive() {}
	virtual void OnDestroy() {}
private:
	void SimulateTimer(int timeDelta)
	{
		_IsSimTimer = true;
		for (auto timerIter = _ListTimer.begin(); timerIter != _ListTimer.end();)
		{
			timerIter->OnSimulate(timeDelta);
			if (timerIter->IsFinish())
			{
				timerIter = _ListTimer.erase(timerIter);
			}
			else
			{
				timerIter++;
			}
		}
		_IsSimTimer = false;
		for (auto delayTimerIter = _DelayTimers.begin(); delayTimerIter != _DelayTimers.end(); delayTimerIter++)
		{
			_ListTimer.push_back(*delayTimerIter);
		}
		_DelayTimers.clear();
	}
private:
	std::list<FFTimer>		_ListTimer;
	std::vector<FFTimer>	_DelayTimers;
	bool					_IsSimTimer;
};

XM_DECLARE_CLASS(FFStateScriptBase)

class FFLuaStateScript : public FFStateScriptBase
{
public:
	FFLuaStateScript() {}
	~FFLuaStateScript() {}
public:
	bool BindLuaScript(lua_State* L);
};