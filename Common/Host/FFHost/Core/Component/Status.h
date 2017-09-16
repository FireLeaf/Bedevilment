/*******************************************************************
  FILE: Status.h
 
  CREATED BY: YangCao , 2017.09.11
 
  HISTORY: 
 
  DESCRIPTION: entity 身上状态数据
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

enum STATUS_FLAG
{
	SF_PHYSIC_IMMUNE		= 1 << 0, // 物理免疫
	SF_MAGIC_IMMUNE			= 1 << 1, // 魔法免疫

};

struct FFStatusComponent 
{
	int				_StuckCount;		// 被控计数
	//STATUS_FLAG		
};