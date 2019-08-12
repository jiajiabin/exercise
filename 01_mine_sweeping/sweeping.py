import random


# 格子类
class grid:
    def __init__(self, num):
        # 是否为墙壁
        self.border = False  # 是否为墙壁
        self.num = num  # 序号
        self.mine = 0  # 地雷数
        self.man = 0  # 玩家数
        self.show = "X"  # 显示图案


# 边缘墙壁类
class border:
    def __init__(self, num):
        self.border = True  # 是否为墙壁
        self.num = num  # 序号
        self.mine = 0  # 地雷数
        self.man = 0  # 玩家数
        self.show = " "  # 显示图案


# 棋盘类
class chessboard:
    def __init__(self):
        self.length = 7  # 棋盘宽
        self.mine_num = 20  # 地雷总数
        self.list = []  # 格子的列表

    # 开始时，放入格子，地雷，墙壁
    def generate_gid(self):
        # 放格子
        for i in range(1, self.length ** 2 + 1):
            self.list.append(grid(i))
        # 放地雷
        list2 = random.sample(self.list, self.mine_num)
        for i in list2:
            i.mine = 1
        # 放墙壁
        for i in range(10):
            self.list.insert(0, border(i))
        for i in range(17, 70, 9):
            for j in range(2):
                self.list.insert(i + j, border(i + j))
        for i in range(81, 92):
            self.list.insert(i, border(i))

    # 修改格子的展示图案
    def show(self):
        for i in range((self.length + 2) ** 2):
            if self.list[i].border is False:
                if self.list[i].man == 1:
                    self.list[i].show = self.list[i - 1].mine + \
                                        self.list[i + 1].mine + \
                                        self.list[i - 3 - self.length].mine + \
                                        self.list[i - 2 - self.length].mine + \
                                        self.list[i - 1 - self.length].mine + \
                                        self.list[i + 1 + self.length].mine + \
                                        self.list[i + 2 + self.length].mine + \
                                        self.list[i + 3 + self.length].mine
                else:
                    self.list[i].show = "X"


# 玩家类
class player:
    def __init__(self):
        self.die = False  # 玩家的死亡状态
        self.player_chess = None  # 玩家的棋盘对局

    # 开始游戏创建对象
    def play(self, str1):
        self.player_chess = str1
        self.player_chess.generate_gid()

    # 玩家移动
    def move(self, str2):
        nums = int(str2[0]) + (int(str2[2])) * 9
        self.player_chess.list[nums].man = 1


# 屏幕类
class screen:
    def __init__(self, ):
        self.user = None

    # 创建使用者对象
    def set_user(self, str):
        self.user = str

    # 显示屏幕方法
    def show_screen(self):
        count = 0
        self.user.show()
        for i in range(81):
            if count != 9:
                print(self.user.list[i].show, end="")
                count += 1
            else:
                print()
                print(self.user.list[i].show, end="")
                count = 1

    # 判断游戏结束
    def game_over(self):
        for i in self.user.list:
            if i.mine == 1 and i.man == 1:
                return 1


while 1:
    # 胜利计数
    counter = 0
    # 创建屏幕
    a001 = screen()
    # 创建棋盘
    chess01 = chessboard()
    # 棋盘对象赋予屏幕
    a001.set_user(chess01)
    # 创建玩家对象
    play01 = player()
    a1 = input("扫雷游戏规则：请按左上角为坐标原点输入扫雷移动坐标，"
               "\n数字显示为当前位置周围8个格子的地雷数之和。\n请确认开始：yes or no。\n")
    # 开始游戏
    if a1 == "yes":
        play01.play(chess01)
        # 展示屏幕
        a001.show_screen()
    elif a1 == "no":
        break
    else:
        print("请重新输入")
        continue
    while 1:
        a2 = input("\n请输入移动指令（x,y）\n")
        if len(a2) == 3 and a2[0] in ["1", "2", "3", "4", "5", "6", "7"] and \
                a2[2] in ["1", "2", "3", "4", "5", "6", "7"]:
            # 玩家移动
            play01.move(a2)
            # 判断游戏结束
            if a001.game_over():
                print("******************************************\n"
                      "*****************游戏结束*****************\n"
                      "******************************************")
                break
            # 展示屏幕
            a001.show_screen()
            counter += 1
            if counter == a001.user.length ** 2 - a001.user.mine_num:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n"
                      "$$$$$$$$$$$$$$$$$游戏胜利$$$$$$$$$$$$$$$$$\n"
                      "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        else:
            a2 = input("\n输入错误，请重新输入移动指令（x,y）")
