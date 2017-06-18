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

using CompSign_t = int;


// 此类用来生成组件标记
template<typename T>
class FFSign
{
private:
	static const int sign = 0;
public:
	static CompSign_t Sign() {
		return static_cast<CompSign_t>(&sign);
	}
};