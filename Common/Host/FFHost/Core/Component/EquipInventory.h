/*******************************************************************
  FILE: EquipInventory.h
 
  CREATED BY: YangCao , 2017.09.11
 
  HISTORY: 
 
  DESCRIPTION: װ����
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

#define EQUIP_INVENTORY_CAPACITY 6//capacity

struct FFEquipInventoryComponent 
{
	int			_EquipID[EQUIP_INVENTORY_CAPACITY];
};

// �¼���

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