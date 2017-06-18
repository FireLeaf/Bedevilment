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

#include <unordered_map>

class FFComponent;

// ������������������
template<typename T>
class FFComponentSign
{
private:
	static const int sign = 0;
public:
	static CompSign_t Sign() {
		return static_cast<CompSign_t>(&sign);
	}
};

/*
	@Class ������ʵ��
*/
class FFEntity : public FFObject
{
public:
	using FFComponentPtr = std::shared_ptr<FFComponent>;
	using ComponentMap = std::unordered_map<CompSign_t, FFComponentPtr>;
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
	FFComponentPtr GetComponentBySign(CompSign_t sign) const
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
public:
	template<typename T>
	void AddComponets()
	{
		AddComonent<T>();
	}

	template<typename T, typename ... Args>
	void AddComponents()
	{
		AddComonent<T>();
		AddComponents<Args...>;
	}

	template<typename Args ... args>
	void CreateFromTemplate()
	{

	}
private:
	virtual void OnCreateObject()
	{

	}

	virtual void OnDestoryObject()
	{

	}
private:
	// ʵ����������
	ComponentMap _EntityComponentMap;
	//std::vector
public:
	inline const FFTransform* Transform() const { return _Transform; }
	inline FFTransform* Transform() { return _Transform; }
private:
	FFTransform* _Transform;
};

#define 

