import option
import random


# 墙
class Wall:
    def __init__(self):
        self.__list = []

    # 创建墙的坐标集
    def __init_points(self):
        for i in range(option.size_x):
            self.__list.append((i, 0))
            self.__list.append((i, option.size_x - 1))
        for j in range(1, option.size_y - 1):
            self.__list.append((0, j))
            self.__list.append((option.size_y - 1, j))

    # 返回墙的坐标
    @property
    def points1(self):
        self.__init_points()
        return self.__list


# 障碍物
class Radblock:
    def __init__(self, ai_point, player_point):
        self.__list = []
        self.init_points(ai_point, player_point)

    # 随机生成障碍物
    def init_points(self, ai_point: list, player_point: list):
        self.__list.clear()
        nums = int((option.size_x * option.size_y) / 3)
        for i in range(nums):
            x = random.randint(1, option.size_x - 2)
            y = random.randint(1, option.size_y - 2)
            if (x, y) in ai_point or (x, y) in player_point:
                continue
            self.__list.append((x, y))

    # 返回墙的坐标
    @property
    def points2(self):
        return self.__list


class Beans:
    def __init__(self, ai_point, radblock_list, player_point):
        self.__point = None
        self.quickly_move(ai_point, radblock_list, player_point)

    # 返回虫子的坐标
    @property
    def point3(self):
        return [self.__point]

    # 随机生成一个坐标
    def quickly_move(self, ai_point: list, radblock_list: list, player_point: list):
        while True:
            # 随机生成虫子的坐标
            x = random.randint(1, option.size_x - 2)
            y = random.randint(1, option.size_y - 2)
            if (x, y) not in ai_point and (x, y) not in radblock_list and (x, y) not in player_point:
                break
        self.__point = (x, y)
