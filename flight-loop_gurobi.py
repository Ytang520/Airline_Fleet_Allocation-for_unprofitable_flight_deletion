"""
Author: Hua Tang
Date:10-13-2022
"""
from gurobipy import *
import datetime
import pandas as pd
import numpy as np
from collections import Counter


def preprocess(path, num1, num2):
    """
    目标：由excel表得到邻接矩阵
    :param path: 文件路径
    :param num1: 考察某类型飞机时，形成DataFrame后，该飞机机型所属飞机的起始位置
    :param num2: 考察某类型飞机时，相乘DataFrame后，该飞机机型所属飞机的终止位置
    :return:
    map_fin : 邻接矩阵
    map_1 : 包含所有的原始数据的邻接矩阵块
    map_name : 得到原始数据对应的邻接矩阵块下每一元素对应的产品号
    """

    df = pd.read_csv(path, encoding="gbk", usecols=['航班号', '考虑不确定性后利润', '区分方法(单位时间成本)'])

    # 讨论第n种飞机的航班环
    data = df.loc[num1:num2]  # num1,num2 分别表示不同飞机环的位置
    flight_list = data['航班号']  # 单独取出航班号列
    od = []  # 目的地集合(名称)
    ob = []  # 出发地集合(名称)

    # 得到所有出发地和目的地的名称
    for i in range(len(flight_list)):
        od.append(flight_list[i][-3:])
        ob.append(flight_list[i][-6:-3])

    length = len(ob)  # 表示产品数目一共多少
    place_stack = []  # 收集所有的地点以及其顺序，并以此顺序为基准构建matrix
    ob_list = []  # get the indexes of the origins
    od_list = []  # get the indexes of the destinations

    for i in range(length):
        if ob[i] not in place_stack:
            place_stack.append(ob[i])
        ob_list.append(place_stack.index(ob[i]))  # get the indexes of the origins

    for i in range(length):
        if od[i] not in place_stack:
            place_stack.append(od[i])
        od_list.append(place_stack.index(od[i]))  # get the indexes of the destinations

    profit = data['考虑不确定性后利润']  # 利润的顺序和ob_list,od_list序号在place_stack中的顺序一致
    city_num = len(place_stack)
    edge_num = max(Counter(ob_list).values())

    matrix = np.full((edge_num, city_num, city_num), float('-inf'))  # 初始化matrix

    # map_1 = [[[float('inf')] for m in range(city_num)] for n in range(city_num)]
    map_name = [[['None'] for m in range(city_num)] for n in range(city_num)]

    # 包含所有权重的原始矩阵块
    for i in range(length):
        row = ob_list[i]
        col = od_list[i]

        for j in range(edge_num):
            if matrix[j][row][col] == float('-inf'):
                matrix[j][row][col] = profit[i]
                break

        # map_1[row][col].append(profit[i])
        map_name[row][col].append(flight_list[i])

    return matrix, map_name


def optimization_new(matrix_need):
    """
    params:
    matrix_need: the matrix needed processing
        which has the size: edge_num * city_num * city*num
    return:
        model: the outcome of the Optimization
    """

    # check the time
    now = datetime.datetime.now
    t = now()

    model = Model("question_optimization")
    city_num = len(matrix_need[0][0])
    edge_num = len(matrix_need[0][0])
    ub_need = matrix_need.shape[0] * matrix_need.shape[2]

    # define the variances
    x = model.addVars(edge_num, city_num, city_num, ub=1, vtype=GRB.BINARY)
    n = model.addVars(city_num, lb=0, ub=ub_need, vtype=GRB.INTEGER)

    # update variances everytime
    model.update()

    # construct the objective
    objsum = 0
    for i in range(city_num):
        for j in range(city_num):
            for k in range(edge_num):
                objsum = objsum + x[k][i][j] * matrix_need[k][i][j]

    model.setObjective(objsum, GRB.MINIMIZE)

    # set the constraints
    for i in range(city_num):
        constraint_1 = sum(x[:, i, :])
        model.addConstr(constraint_1 == n[i])

    for j in range(city_num):
        constraint_2 = sum(x[:, :, j])
        model.addConstr(constraint_2 == n[j])

    model.optimize()

    print('Time_needed: %s' % (now() - t))

    return model
