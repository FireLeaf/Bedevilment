/*******************************************************************
  FILE: Status.h
 
  CREATED BY: YangCao , 2017.09.11
 
  HISTORY: 
 
  DESCRIPTION: entity ����״̬����
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

enum STATUS_FLAG
{
	SF_PHYSIC_IMMUNE		= 1 << 0, // ��������
	SF_MAGIC_IMMUNE			= 1 << 1, // ħ������

};

struct FFStatusComponent 
{
	int				_StuckCount;		// ���ؼ���
	//STATUS_FLAG		
};