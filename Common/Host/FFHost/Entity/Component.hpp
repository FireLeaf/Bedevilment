/*
* FILE: Component.hpp
*
* DESCRIPTION:
*
* CREATED BY: Owl Yang, 2017/5/20
*
* HISTORY:
*
* Copyright (t) 2016 FF Studio, All Rights Reserved.
*/

#pragma once

#define DECLARE_COMPONENT(Component) \
	private:\
		static const std::string ComponentName;\
	public:\
		virtual const std::string& GetName() override const;

#define IMPLEMENT_COMPONENT(Component) \
	const std::string FF##Component::ComponentName = #Component;\
	const std::string& FF##Component::GetName() const{\
		return ComponentName;\
	}\
	CompSign_t GetSign() const {\
		return FFComponentSign<FF##Component>::Sign();
	}

class FFEntity;

class FFComponent : public FFObject
{
	friend class FFEntity;
public:
	FFComponent(FFEntity* Entity) : _Entity(Entity) {}
private:
	virtual ~FFComponent() {} // 只有Entity才有权限调用
private:
	virtual bool OnInitialize() = 0;
	virtual void OnTick(int TimeDelta) = 0;
	virtual void OnDestroy() = 0;
	virtual void OnActive() = 0;
	virtual void OnDeactive() = 0;
public:
	FFEntity*	GetEntity() { return _Entity; }
	void		SetActive(bool Active)
	{
		if (_Active != _Active)
		{
			_Active = Active;
			if (_Active)
				OnActive();
			else
				OnDeactive();
		}
	}
public:
	virtual const std::string& GetName() const = 0;
	virtual CompSign_t GetSign() const = 0;
public:
	//FFComponent()
private:
	FFEntity*				_Entity = nullptr;
	bool					_Active = false;
};