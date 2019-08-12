# A*算法，多态继承
# 初始信息定义，外侧调用需继承并重写
class Init_Delegate:
    def __init__(self):
        self.__start = None  # 起点坐标         (x, y)
        self.__end = None  # 终点坐标         (x, y)
        self.__close_list = []  # 墙壁坐标列表     [(x, y),(x, y)。。。。。。]
        self.__map_border = []  # 地图边界,存地图左上原点，右下极点两点坐标     [(x, y),(x, y)]

    @property
    def map_border(self):
        return self.__map_border

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    @property
    def close_list(self):
        return self.__close_list


map_border = []
end = None


# 节点类（管理父节点，节点坐标，节点FGH三值)
class Node:
    def __init__(self, father, x, y):
        global map_border, end
        # 判断（x， y）坐标未超限
        if x < map_border[0][0] or x > map_border[1][0] \
                or y < map_border[0][1] or y > map_border[1][1]:
            raise Exception("坐标错误")
        self.__father = father
        self.__x, self.__y = x, y
        # 判断初始点，定义FGH三值
        if self.__father != None:
            self.__G = self.__father.G + 1
            self.__H = self.__calculate_h(end)
            self.__F = self.__G + self.__H
        else:
            self.__G = 0
            self.__H = 0
            self.__F = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def F(self):
        return self.__F

    @property
    def G(self):
        return self.__G

    @property
    def father(self):
        return self.__father

    # 计算H值
    def __calculate_h(self, end):
        return abs(self.__x - end[0][0]) + abs(self.__y - end[0][1])

    # 发生绕路时，重设父节点，刷新最短路径
    def reset_father(self, father, new_G):
        if father != None:
            self.__G = new_G
            self.__F = self.__G + self.__H
        self.__father = father


class Find_Way:
    def __init__(self):
        # 导入代理对象
        self.__delegate = None
        # 定义开始、结束节点
        self.__start_node = None
        self.__end_node = None
        self.__open_dict = {}  # 开放坐标字典表，点坐标、点节点作为键值对存储  {(x, y):Node}
        self.__close_dict = {}  # 关闭坐标字典表，点坐标、点节点作为键值对存储  {(x, y):Node}
        self.__short_way = []  # 最短路线的坐标列表

    @property
    def short_way(self):
        return self.__short_way

    # 创建关闭坐标字典表
    def __set_close_dict(self):
        for i in self.__delegate.close_list:
            close_node = Node(None, i[0], i[1])
            self.__close_dict[i[0], i[1]] = close_node

    # 寻路函数，外侧调用
    def find_way(self, delegate: Init_Delegate):
        self.__open_dict.clear()
        self.__close_dict.clear()
        global map_border, end
        self.__delegate = delegate
        map_border = self.__delegate.map_border
        end = self.__delegate.end
        # 定义开始、结束节点
        self.__start_node = Node(None, self.__delegate.start[0][0], self.__delegate.start[0][1])
        self.__end_node = Node(None, self.__delegate.end[0][0], self.__delegate.end[0][1])
        self.__set_close_dict()
        # 从起点开始寻路
        self.__open_dict[self.__delegate.start[0]] = self.__start_node
        the_now_node = self.__start_node
        # try:
        # 循环以当前节点与终点比较，找到最短路径
        while self.__addAdjacentIntoOpen(the_now_node):
            the_now_node = self.__min_F_node()
        self.__recursive_way(self.__end_node)
        return self.short_way
        # except Exception as err:
        #     # 若无路，则调用外侧函数，默认pass
        #     return []

    # 寻找F值最小的节点
    def __min_F_node(self):
        # 自定义无路错误
        if len(self.__open_dict) == 0:
            self.__short_way = []
            return 1
        # 比较F值并将节点列为当前节点，进行下一个循环比较
        min1 = 999999999999999999999999
        short_x_y = self.__delegate.start[0]
        for x_y, node in self.__open_dict.items():
            if min1 > node.F:
                min1 = node.F
                short_x_y = x_y
        return self.__open_dict[short_x_y]

    # 将当前节点的周围点（上下左右4个，默认不可走斜线）加入开放坐标字典表
    def __addAdjacentIntoOpen(self, the_now_node):
        if the_now_node == 1:
            return False
        # 将当前节点从开放（坐标字典表）中移除，加入关闭（坐标字典表）
        self.__open_dict.pop((the_now_node.x, the_now_node.y))
        self.__close_dict[(the_now_node.x, the_now_node.y)] = the_now_node
        # 添加周围节点列表
        round_list = []
        try:
            round_list.append(Node(the_now_node, the_now_node.x - 1, the_now_node.y))
        except Exception as e:
            pass
        try:
            round_list.append(Node(the_now_node, the_now_node.x + 1, the_now_node.y))
        except Exception as e:
            pass
        try:
            round_list.append(Node(the_now_node, the_now_node.x, the_now_node.y - 1))
        except Exception as e:
            pass
        try:
            round_list.append(Node(the_now_node, the_now_node.x, the_now_node.y + 1))
        except Exception as e:
            pass
        # 判断周围节点列表中各点
        for i in round_list:
            # 如果是终点，重设当前节点为终点的父节点,并打断寻路循环
            if i.x == self.__delegate.end[0][0] and i.y == self.__delegate.end[0][1]:
                self.__end_node.reset_father(the_now_node, the_now_node.G + 1)
                return False
            # 如果在关闭坐标字典表中，跳过
            elif (i.x, i.y) in self.__close_dict:
                continue
            # 如果不在开放坐标字典表中，加入
            elif (i.x, i.y) not in self.__open_dict:
                self.__open_dict[(i.x, i.y)] = i
            # 如果存在在open_list中，通过G值判断此点是否为近路
            # (若the_now_node的G值+1更小说明原开放字典表中的节点为绕远路与此点相交)，重设父节点（重载路线）
            else:
                open_list_node = self.__open_dict[(i.x, i.y)]
                if open_list_node.G > (the_now_node.G + 1):
                    open_list_node.reset_father(the_now_node, the_now_node.G + 1)
        return True

    # 递归返回最短路线坐标集合
    def __recursive_way(self, node: Node):
        if node.father == None:
            return
        self.__short_way.insert(0, (node.x, node.y))
        self.__recursive_way(node.father)
