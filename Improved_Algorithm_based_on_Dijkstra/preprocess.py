import pandas as pd


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
    od = []  # 目的地
    ob = []  # 出发地

    # 得到所有出发地和目的地的名称
    for i in range(len(flight_list)):
        od.append(flight_list[i][-3:])
        ob.append(flight_list[i][-6:-3])

    length = len(ob)  # 表示产品数目一共多少
    ob_stack = []  # 收集所有的地点以及其顺序，并以此顺序为准
    ob_list = []
    od_list = []
    for i in range(length):
        if ob[i] not in ob_stack:
            ob_stack.append(ob[i])
        ob_list.append(ob_stack.index(ob[i]))

    for i in range(length):
        if od[i] not in ob_stack:
            ob_stack.append(od[i])
        od_list.append(ob_stack.index(od[i]))

    profit = data['考虑不确定性后利润']  # 利润的顺序和ob_list,od_list的顺序一致
    length_place = len(ob_stack)
    map_1 = [[[float('inf')] for m in range(length_place)] for n in range(length_place)]
    map_name = [[['None'] for m in range(length_place)] for n in range(length_place)]

    # 包含所有权重的原始矩阵块
    for i in range(length):
        row = ob_list[i]
        col = od_list[i]
        map_1[row][col].append(profit[i])
        map_name[row][col].append(flight_list[i])

    # 构造邻接矩阵
    map_fin = [[0 for m in range(len(ob_stack))] for n in range(len(ob_stack))]

    for index_row in range(length_place):
        for index_col in range(length_place):
            min_profit = min(map_1[index_row][index_col])
            map_fin[index_row][index_col] = min_profit

    return map_fin, map_1, map_name
