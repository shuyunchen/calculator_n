#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/14 23:50
# @Author  : 陈庆云
# @File    : test_calc_new.py
# @Software: PyCharm
import pytest


class Test_Calculator:

    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_add_datas):
        res = None
        try:
            res = get_calc.add(get_add_datas[0], get_add_datas[1])
            if isinstance(res, float):
                res = round(res, 2)
            print(f'计算结果为：{res}')
        except Exception as e:
            print(e)
        assert res == get_add_datas[2]

    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div_datas):
        res = None
        try:
            res = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(res, float):
                res = round(res, 2)
            print(f'计算结果为：{res}')
        except Exception as e:
            print(e)
        assert res == get_div_datas[2]

    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub_datas):
        res = None
        try:
            res = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            if isinstance(res, float):
                res = round(res, 2)
            print(f'计算结果为：{res}')
        except Exception as e:
            print(e)
        assert res == get_sub_datas[2]

    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_mul_datas):
        res = None
        try:
            res = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            if isinstance(res, float):
                res = round(res, 2)
            print(f'计算结果为：{res}')
        except Exception as e:
            print(e)
        assert res == get_mul_datas[2]
