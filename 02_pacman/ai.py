import findway
import option
import randomwall


class Ai(findway.Init_Delegate):
    def __init__(self):
        self.__point = [(2, 2)]  # 点坐标
        super().__init__()
        self.__start = self.__point  # 起点坐标，自身的位置        (x, y)
        self.__end = None  # 终点坐标，豆子的位置        (x, y)
        self.__close_list = []  # 墙壁坐标列表     [(x, y),(x, y)。。。。。。]
        # 地图边界,存地图左上原点，右下极点两点坐标     [(x, y),(x, y)]
        self.__map_border = [(1, 1), (option.size_x - 2, option.size_y - 2)]
        self.__find_way = findway.Find_Way()
        self.__short_way = []
        # 图形界面清屏
        self.__exchange = 1

    # 返回ai的坐标
    @property
    def points(self):
        return self.__point

    @property
    def exchange(self):
        return self.__exchange

    @exchange.setter
    def exchange(self, exchange):
        self.__exchange = exchange

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

    # 按寻路结果移动
    def __move(self):
        self.__short_way = self.__find_way.find_way(self)
        if self.__short_way == []:
            return
        self.__point[0] = (self.__short_way[0][0], self.__short_way[0][1])

    # ai每帧的行为
    def action(self, radblock: randomwall.Radblock, beans: randomwall.Beans, player_point):
        self.__start = self.__point
        self.__end = beans.point3
        self.__close_list = radblock.points2
        self.__move()
        self.__exchange = 0
        if self.__dead() or self.__start == self.__end:
            radblock.init_points(self.__point, player_point)
            beans.quickly_move(self.__point, radblock.points2, player_point)
            self.__exchange = 1

    # 判定无路可走
    def __dead(self):
        if self.__short_way == []:
            return True
        return False
