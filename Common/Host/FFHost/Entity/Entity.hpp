/*
* FILE: Entity.h
*
* DESCRIPTION: Scene object base class
*
* CREATED BY: Owl Yang, 2017/5/20
*
* HISTORY:
*
* Copyright (t) 2016 FF Studio, All Rights Reserved.
*/

#pragma once

class FFComponent;

// 此类用来生成组件标记
template<typename T>
class FFComponentSign
{
public:
	static CompSign_t Sign() {
		return 0;
	}
};

/*
	@Class 场景中实体
*/
class FFEntity : public FFMemMonitored
{
public:
	using ComponentMap = std::unordered_map<CompSign_t, FFComponent*>;
public:
	// 根据类型来获取组件
	template<typename T>
	T* GetComponent()
	{
		FFComponent* component = GetComponentBySign(FFComponentSign<T>::Sign());
		return dynamic_cast<T>(component);
	}

	// 根据组件名字来获取组件
	FFComponent* GetComponent(const std::string& componentName)
	{
		for (auto ComponentIter : _EntityComponentMap)
		{
			FFComponent* component = ComponentIter->second;
			if (component->GetName() == componentName)
			{
				return component;
			}
		}
		return nullptr;
	}

	// 根据类型添加模板
	template<typename T>
	T* AddComonent()
	{
		T* component = GetComponent<T>();
		if (component)
			return component;
		
		component = new T(this);
		_EntityComponentMap[FFComponentSign<T>::Sign()] = component;
		component->OnInitialize();
		component->SetActive(true);
	}

	// 移除模板
	template<typename T>
	void RemoveComponent()
	{
		T* component = GetComponent<T>();
		if (component)
		{
			component->SetActive(false);
			component->OnDestroy();
			EraseComponentBySign(FFComponentSign<T>::Sign());
			delete component;
		}
	}
public:
	void Tick(int TimeDelta);

private:
	// 通过组件标签来获取组件
	FFComponent* GetComponentBySign(CompSign_t sign) const
	{
		auto CompIter = _EntityComponentMap.find(sign);
		if (CompIter != _EntityComponentMap.end())
		{
			return CompIter.second;
		}
		return nullptr;
	}

	void EraseComponentBySign()
	{
		auto CompIter = _EntityComponentMap.find(sign);
		if (CompIter != _EntityComponentMap.end())
		{
			_EntityComponentMap.erase(CompIter);
		}
	}

private:
	// 实体上面的组件
	ComponentMap _EntityComponentMap;
	//std::vector
};

