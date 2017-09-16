/*******************************************************************
  FILE: StateScriptBase.h
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: 状态脚本基类
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
  *******************************************************************/

#pragma once

#include "TypeDef.h"
#include "lua.h"

#include <functional>

struct FFFrameEvent 
{
public:
	void OnSimulate(int curFrame)
	{
		if (_KeepOn)
		{
			_FrameHandler();
		}
		else
		{
			if (_Frame == curFrame)
			{
				_IsFinish = true;
				_FrameHandler();
			}
		}
	}
private:
	bool						_IsFinish;
	int							_Frame;
	bool						_KeepOn;
	std::function<void(int)>	_FrameHandler;
};

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

enum STATE_SCRIPT_STATUS
{
	SSS_RUNGING,	// 当前运行中
	SSS_STOP,		// 被终止
	SSS_FINISHED,	// 完成
};

class FFStateScriptBase
{
public:
	FFStateScriptBase(Entity) {}
	virtual ~FFStateScriptBase() {}
public:
	void AddStateTimer(int peroid, bool isOnce, std::function<void()> timerHandler) {
		FFTimer timer(peroid, isOnce, timerHandler);
		if (_IsSimTimer)
			_DelayTimers.emplace_back(timer);
		else
			_ListTimer.emplace_back(timer);
	}

	bool IsRunning() const { return _StateStatus == SSS_RUNGING; }
	void Stop() {
		if (!IsRunning()) return;
		_StateStatus = SSS_RUNGING;
		OnStop();
	}
	void Finish() {
		if (!IsRunning()) return;
		_StateStatus = SSS_FINISHED;
		OnFinish();
	}
public:
	void Simulate(int timeDelta)
	{
		OnSimulate(timeDelta);

		_TimeToLive -= timeDelta;
		if (_TimeToLive <= 0)
		{
			Finish();
		}
	}
public:
	virtual void OnCreate() {}
	virtual void OnActive() { _CurFrame = 0; }
	virtual void OnSimulate(int timeDelta)
	{
		SimulateTimer(timeDelta);
		SimulateFrame();
		_CurFrame++;

		_TimeToLive -= timeDelta;
		if (_TimeToLive <= 0)
		{
			Finish();
		}
	}
	virtual void OnDeactive() {}
	virtual void OnDestroy() {}
private:
	virtual void OnStop() {} // 在被中止的时候调用
	virtual void OnFinish() {} // 在正常完成调用
private:
	void SimulateFrame()
	{

	}

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
	STATE_SCRIPT_STATUS		_StateStatus;
	int						_CurFrame;
	std::list<FFFrameEvent>	_ListFrameEvent;
	
	int						_LifeTime;
	int						_TimeToLive;
};

XM_DECLARE_CLASS(FFStateScriptBase)

class FFLuaStateScript : public FFStateScriptBase
{
public:
	FFLuaStateScript() {}
	~FFLuaStateScript() {}
public:
	bool BindLuaScript(lua_State* L);
public:
	virtual void OnCreate() {
		FFStateScriptBase.OnCreate();
		
		// write here
		lua_gettable(L, LUA_REGISTRYINDEX, _RefInstance);
		lua_getfield(L, -1, "OnCreate");
		lua_pcall(L, 0, 0, -1);
	}

	virtual void OnActive() {
		FFStateScriptBase.OnActive();
		
		// write here

	}

	virtual void OnSimulate(int timeDelta)
	{
		FFStateScriptBase.OnSimulate(timeDelta);
		if (!IsRunning()) return;

		if (_RefSimulate != 0)
		{
			lua_rawgeti(L, LUA_REGISTRYINDEX, _RefSimulate);
			lua_pcall();//....
		}
	}

	virtual void OnDeactive() {
		// write here

		FFStateScriptBase.OnDeactive();
	}

	virtual void OnDestroy() {
		// write here

		FFStateScriptBase.OnDestroy();
	}
private:
	virtual void OnStop() { // 在被中止的时候调用
		
	}
	virtual void OnFinish() { // 在正常完成调用
		
	}
private:
	int					_RefInstance;
	int					_RefSimulate;
};