/*******************************************************************
  FILE: Property.h
 
  CREATED BY: YangCao , 2017.09.11
 
  HISTORY: 
 
  DESCRIPTION: �������
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

struct FFPropertyComponent 
{
	int				_HP;				// Ѫ��
	short			_MP;				// ħ��ֵ
	short			_XP;				// XPֵ
	int				_PhysicAttack;		// ������
	int				_MagicAttack;		// ħ������
	int				_PhysicDefence;		// �������
	int				_MagicDefence;		// ħ������
	int				_PhysicCrit;		// ������
	int				_MagicCrit;			// ħ������
	int				_PhysicAntiCrit;	// �����ⱬ��
	int				_MagicAntiCrit;		// ħ���ⱬ��
	int				_PhysicPenetrate;	// ����͸
	int				_MagicPenetrate;	// ħ����͸

	int				
};

/*
	���Լ���
	A �������� = �������� * lv + �����̶��������ԣ��������֮�����߰���ģ�
	B װ������ = A * (b11 + b12 + ... + b1n) + (b21 + ... + b2n)
	C ״̬���� = A * (c11 + c12 + ... + c1n) + (c21 + ... + c2n)

	��������
	A + B + C
*/