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

// ������������������
template<typename T>
class FFComponentSign
{
public:
	static CompSign_t Sign() {
		return 0;
	}
};

/*
	@Class ������ʵ��
*/
class FFEntity : public FFMemMonitored
{
public:
	using ComponentMap = std::unordered_map<CompSign_t, FFComponent*>;
public:
	// ������������ȡ���
	template<typename T>
	T* GetComponent()
	{
		FFComponent* component = GetComponentBySign(FFComponentSign<T>::Sign());
		return dynamic_cast<T>(component);
	}

	// ���������������ȡ���
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

	// �����������ģ��
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

	// �Ƴ�ģ��
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
	// ͨ�������ǩ����ȡ���
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
	// ʵ����������
	ComponentMap _EntityComponentMap;
	//std::vector
};

