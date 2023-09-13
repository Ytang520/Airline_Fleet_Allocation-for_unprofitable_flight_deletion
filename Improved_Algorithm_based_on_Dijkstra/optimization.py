def min_dis_1(lamda, dis, graph):
    """
    目标：求某地到某地的中间步骤
    params:
    lamda : 具体路径
    dis : dis为最优化距离矩阵
    vnum : vnum为(包括自己在内)所有到达位置的数目之和，等于图的维数
    graph : 原图
    """
    inspection = []  # 判断确实已经得到了最短路
    while True:
        vnum = len(graph)
        for k in range(vnum):
            # k 为已在的位置
            for j in range(vnum):
                # j 为即将前进的位置
                if j not in lamda[k]:  # i!=j隐含其间(因为前限定lamda必然包含i)，阻止了回到出发点
                    if dis[j] > dis[k] + graph[k][j]:
                        tmp_val = dis[j]
                        # 临时储存dis[j],表示未有k时，i->j的最短路径
                        dis[j] = dis[k] + graph[k][j]
                        lamda[j].clear()
                        lamda[j].extend(lamda[k])
                        lamda[j].append(j)
                        for num in range(vnum):
                            if num == j or num == k:
                                continue
                            elif j in lamda[num]:  # 判断lamda[num]是否需要拼接(即矩阵元素里是否含有j元素)
                                j_id = lamda[num].index(j)
                                if not [x for x in lamda[j] if x in lamda[num][j_id+1:]]:
                                    # 判断拼接后的矩阵是否 没成环，没成环，则拼接；反之，放弃拼接
                                    del lamda[num][:j_id + 1]
                                    tmp = lamda[j][:]
                                    tmp.extend(lamda[num])
                                    lamda[num].clear()
                                    lamda[num].extend(tmp)
                                    del tmp
                                    dis[num] = dis[num] - tmp_val + dis[j]
        inspection.append(dis)
        if len(inspection) > 1:
            if inspection[-1] == inspection[-2]:
                break

    return 0


def min_dis(graph, dot):
    """目标：得到从节点dot出发，到非dot点的最短距离所走过的具体路径和相应权重之和
    params:
    graph：输入的邻接矩阵
    dot：起始点
    """
    vnum = len(graph)  # vnum为(包括自己在内)所有到达位置的数目之和
    dis = [graph[dot][h] for h in range(vnum)]  # dis为最优化矩阵
    lamda = [[dot] for h in range(vnum)]  # 初始化具体路径，此处设定包含到自己
    # 考虑到dis已经有距离，此时对lamda进行填充
    for h in range(vnum):
        if dis[h] < float('inf'):
            lamda[h].append(h)
    min_dis_1(lamda, dis, graph)

    return lamda, dis


def min_circle_dot(graph, dot):
    """
    目的：得到经过i点的最小环
    方法：把lamda(路径)中一开始的dot去掉(改为未访问)，再跑一次上面的最短路得到
    :params:
    graph: 原图
    i：起始点
    :return:
    road: 最短路路径
    distance: 最短路距离
    """
    lamda, dis = min_dis(graph, dot)
    vnum = len(graph)
    for i in range(vnum):
        del lamda[i][0]
    min_dis_1(lamda, dis, graph)
    # 下中road是自dot出发的最小环具体路径，distance是最短路径
    road = [dot]
    road.extend(lamda[dot])
    distance = dis[dot]
    return road, distance


def min_circle_graph(graph):
    """
    目的：得到整张图最短路
    :param graph:输入图
    :return:
    """
    road = []
    distance = []
    for i in range(len(graph)):
        road_1, distance_1 = min_circle_dot(graph, i)
        road.append(road_1)
        distance.append(distance_1)
    index = distance.index(min(distance))
    road_fin = road[index]
    distance_fin = distance[index]

    return road_fin, distance_fin
