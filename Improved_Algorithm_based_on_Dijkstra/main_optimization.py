from optimization import *
from preprocess import *


def type_profit(path, num1, num2):
    # 得到邻接矩阵
    graph, graph_origin, map_name = preprocess(path, num1, num2)

    # 处理邻接矩阵
    graph_copy = graph[:][:]
    graph_origin_copy = graph_origin[:][:][:]
    road, distance = min_circle_graph(graph_copy)
    sum_distance = []
    name_list = []  # name_list记录删除环的产品号

    while distance < 0:
        length = len(road)
        name_list_1 = []  # name_list_1代表每一环删除的产品号
        for i in range(length):
            if i + 1 < length:
                row = road[i]
                col = road[i + 1]
                index = graph_origin_copy[row][col].index(graph_copy[row][col])
                name_list_1.append(map_name[row][col][index])
                graph_origin_copy[row][col].remove(graph_copy[row][col])
                map_name[row][col].remove(map_name[row][col][index])
                graph_copy[row][col] = min(graph_origin_copy[row][col])  # graph_origin_copy的数值填充入graph_copy
        name_list.append(name_list_1)
        sum_distance.append(distance)
        print(name_list_1, distance)
        del road
        del distance
        road, distance = min_circle_graph(graph_copy)

    print("We have deleted these roads/circles:")
    print(name_list)
    print("Their profits/weights are:")
    print(sum_distance)
    print("The sum of the profits/weights is")
    print(sum(sum_distance), '\n')


# 参数输入,不同机型的分配
# 第四种机型, excel上位置147
path_1 = 'F12C12Y48.csv'
num1_1 = 0
num2_1 = 145
# 第六种机型, excel上位置343
path_2 = 'F0C0Y76.csv'
num1_2 = 0
num2_2 = 341
# 第六种机型, excel上位置305
path_3 = 'F16C0Y165.csv'
num1_3 = 0
num2_3 = 303

type_profit(path_1, num1_1, num2_1)
type_profit(path_2, num1_2, num2_2)
type_profit(path_3, num1_3, num2_3)
