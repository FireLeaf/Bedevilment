/*******************************************************************
  FILE: Map.h
 
  CREATED BY: YangCao , 2017.09.09
 
  HISTORY: 
 
  DESCRIPTION: ��ͼ�������
 
  Copyright (c) 2017 FF Studio, All Rights Reserved .
*******************************************************************/

#pragma once

enum MAP_GRID_FLAG
{
	MGF_WALKABLE		= 1 << 0, // �����ߵ�
	MGF_SWIMABLE		= 1 << 1, // ����Ӿ��
	MGF_AIRABLE			= 1 << 2, // �ɷ��е�
	MGF_ROADBLOCK		= 1 << 3, // ��ʱ·��
	MGF_BLOCK			= 1 << 3, // ������
};

enum CAMP_MASK
{
	CM_PLAYER1			= 1 << 0, // A��
	CM_PLAYER2			= 1 << 1, // B��
	CM_PLAYER3			= 1 << 2, // C��

	MAX_CAMP_COUNT		= 10,
};

struct FFMapGrid 
{
	MAP_GRID_FLAG		_MapGridFlag;					// ��ǰ��ͼ���ӵı��
	unsigned char		_Visibility[MAX_CAMP_COUNT];	// ��ǰ���ӵĿɼ���
};

struct FFMapComponent 
{
	int			_MapWidth;	// ��ͼ���
	int			_MapLength;	// ��ͼ����
	FFMapGrid**	_MapGrids;	// ��ͼ�߼�����
};