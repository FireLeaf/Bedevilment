/*******************************************************************
  FILE: Property.h
 
  CREATED BY: YangCao , 2017.09.11
 
  HISTORY: 
 
  DESCRIPTION: 属性组件
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

struct FFPropertyComponent 
{
	int				_HP;				// 血量
	short			_MP;				// 魔法值
	short			_XP;				// XP值
	int				_PhysicAttack;		// 物理攻击
	int				_MagicAttack;		// 魔法攻击
	int				_PhysicDefence;		// 物理防御
	int				_MagicDefence;		// 魔法防御
	int				_PhysicCrit;		// 物理暴击
	int				_MagicCrit;			// 魔法暴击
	int				_PhysicAntiCrit;	// 物理免爆击
	int				_MagicAntiCrit;		// 魔法免爆击
	int				_PhysicPenetrate;	// 物理穿透
	int				_MagicPenetrate;	// 魔法穿透

	int				
};

/*
	属性计算
	A 基本属性 = 基础属性 * lv + 其它固定基础属性（例如符文之类乱七八糟的）
	B 装备属性 = A * (b11 + b12 + ... + b1n) + (b21 + ... + b2n)
	C 状态属性 = A * (c11 + c12 + ... + c1n) + (c21 + ... + c2n)

	最终属性
	A + B + C
*/