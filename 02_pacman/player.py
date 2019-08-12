import option
import randomwall
import ai


# 玩家类
class Player:
    def __init__(self):
        # 坐标
        self.__point = [(option.size_x - 3, option.size_y - 3)]
        # 方向
        self.__toward = (0, 1)

    # 返回ai的坐标
    @property
    def points(self):
        return self.__point

    def set_toward(self, new_toward):
        dictionary = {'shang': (0, -1), 'xia': (0, 1), 'zuo': (-1, 0), 'you': (1, 0)}
        target_toward = dictionary[new_toward]
        self.__toward = target_toward

    def __move(self, ai_point, wall_point, radblock_points):
        noway_list = []
        noway_list.extend(ai_point)
        noway_list.extend(wall_point)
        noway_list.extend(radblock_points)
        if (self.__point[0][0] + self.__toward[0], self.__point[0][1] + self.__toward[1]) in noway_list:
            return
        self.__point[0] = (self.__point[0][0] + self.__toward[0], self.__point[0][1] + self.__toward[1])

    def action(self, ai: ai.Ai, radblock: randomwall.Radblock, beans: randomwall.Beans, wall: randomwall.Wall):
        self.__move(ai.points, wall.points1, radblock.points2)
        if self.__point == beans.point3:
            ai.exchange = 1
            radblock.init_points(ai.points, self.__point)
            beans.quickly_move(ai.points, radblock.points2, self.__point)
