import option
import os


class Displayer:
    def __init__(self):
        # 墙坐标列表
        self.__wall_list = []

    # 导入墙的坐标点数据
    def extend_points(self, point_list):
        self.__wall_list.extend(point_list)

    # 刷新清空坐标列表
    def clear(self):
        self.__wall_list.clear()

    # 打印图形，自身的墙，ai的点，豆子的点
    def draw__graphics(self, ai_points, radblock_points2, beans_point):
        os.system("cls")
        print("".center(option.size_x * 2, "="))
        for j in range(option.size_y):
            for i in range(option.size_x):
                if (i, j) in self.__wall_list:
                    print("田", end="")
                elif (i, j) in radblock_points2:
                    print("田", end="")
                elif (i, j) in ai_points:
                    print("○", end="")
                elif (i, j) in beans_point:
                    print("※", end="")
                else:
                    print("  ", end="")
            print()
        print("".center(option.size_x * 2, "="))
