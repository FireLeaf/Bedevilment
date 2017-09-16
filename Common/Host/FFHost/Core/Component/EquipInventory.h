/*******************************************************************
  FILE: EquipInventory.h
 
  CREATED BY: YangCao , 2017.09.11
 
  HISTORY: 
 
  DESCRIPTION: 装备栏
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

#define EQUIP_INVENTORY_CAPACITY 6//capacity

struct FFEquipInventoryComponent 
{
	int			_EquipID[EQUIP_INVENTORY_CAPACITY];
};

// 事件有

struct EntityAddEquip 
{
	int			_EquipSlot;
	int			_EquipID;
};

struct EntityRemoveEquip 
{
	int			_EquipSlot;
	int			_EquipID;
};