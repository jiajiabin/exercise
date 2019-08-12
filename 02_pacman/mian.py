import randomwall
from displayer import Displayer
from ai import Ai
import time
import threading
import msvcrt

displayer = Displayer()
wall = randomwall.Wall()
ai = Ai()
radblock = randomwall.Radblock(ai.points)
beans = randomwall.Beans(ai.points, radblock.points2)

running = True


class InputThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global running
        while running:
            c = str(msvcrt.getch())
            if c == "b'q'":
                running = False


input_thread = InputThread()
input_thread.start()
count = 0
while running:
    # ai设定n帧移动一次
    if count > 0:
        death = ai.action(radblock, beans)
        count = 0
    count += 1

    # 将墙的坐标导入
    displayer.extend_points(wall.points1)

    # 绘制图像
    displayer.draw__graphics(ai.points, radblock.points2, beans.point3)
    # 清屏
    displayer.clear()
    # time.sleep(snake.sleep_time)
    time.sleep(1)
