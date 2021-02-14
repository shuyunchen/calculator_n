#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/14 23:51
# @Author  : 陈庆云
# @File    : conftest.py
# @Software: PyCharm
import os

import pytest
import yaml

from pythoncode.Calculator import Calculator


@pytest.fixture(scope='module')
def get_calc():
    print("\n【获取计算器实例】")
    calc = Calculator()
    return calc


def get_yaml_data():
    yaml_file_path = os.path.dirname(__file__) + '\\testdata.yaml'
    with open(yaml_file_path, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas


@pytest.fixture(params=get_yaml_data()["add_datas"], ids=get_yaml_data()["add_myids"])
def get_add_datas(request):
    add_datas = request.param
    print("\n【开始计算】")
    yield add_datas
    print("\n【计算结束】")


@pytest.fixture(params=get_yaml_data()["sub_datas"], ids=get_yaml_data()["sub_myids"])
def get_sub_datas(request):
    add_datas = request.param
    print("\n【开始计算】")
    yield add_datas
    print("\n【计算结束】")


@pytest.fixture(params=get_yaml_data()["div_datas"], ids=get_yaml_data()["div_myids"])
def get_div_datas(request):
    add_datas = request.param
    print("\n【开始计算】")
    yield add_datas
    print("\n【计算结束】")


@pytest.fixture(params=get_yaml_data()["mul_datas"], ids=get_yaml_data()["mul_myids"])
def get_mul_datas(request):
    add_datas = request.param
    print("\n【开始计算】")
    yield add_datas
    print("\n【计算结束】")
