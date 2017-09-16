/*******************************************************************
  FILE: Map.h
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: 地图数据组件
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

enum MAP_GRID_FLAG
{
	MGF_WALKABLE		= 1 << 0, // 可行走的
	MGF_SWIMABLE		= 1 << 1, // 可游泳的
	MGF_AIRABLE			= 1 << 2, // 可飞行的
	MGF_ROADBLOCK		= 1 << 3, // 临时路障
	MGF_BLOCK			= 1 << 3, // 阻塞的
};

enum CAMP_MASK
{
	CM_PLAYER1			= 1 << 0, // A方
	CM_PLAYER2			= 1 << 1, // B方
	CM_PLAYER3			= 1 << 2, // C方

	MAX_CAMP_COUNT		= 10,
};

struct FFMapGrid 
{
	MAP_GRID_FLAG		_MapGridFlag;					// 当前地图格子的标记
	unsigned char		_Visibility[MAX_CAMP_COUNT];	// 当前格子的可见性
};

struct FFMapComponent 
{
	int			_MapWidth;	// 地图宽度
	int			_MapLength;	// 地图长度
	FFMapGrid**	_MapGrids;	// 地图逻辑格子
};