import tkinter
import option
import time
import randomwall
from displayer import Displayer
from ai import Ai
import threading
import player

# 创建所有对象
displayer = Displayer()
wall = randomwall.Wall()
ai = Ai()
player = player.Player()
radblock = randomwall.Radblock(ai.points, player.points)
beans = randomwall.Beans(ai.points, radblock.points2, player.points)
# player方向
fangxiang = "xia"
# 创建一把锁
lock = threading.Lock()

# 打开一个窗口
window = tkinter.Tk()
# 设置标题
window.title("吃豆大战")
# 设置大小
size = str(option.size_x * 23) + 'x' + str(option.size_y * 25 + 50)
window.geometry(size)
# 在图形界面上创建画布并放置各种元素
canvas = tkinter.Canvas(window, bg='white', height=option.size_x * 20 + 1, width=option.size_y * 20 + 1)


def aimove():
    count = 0
    while 1:
        # ai设定n帧移动一次
        if count > 0:
            ai.action(radblock, beans, player.points)
            count = 0
        count += 1
        # time.sleep(snake.sleep_time)
        chidouren = ai.points[0]
        image_file2 = tkinter.PhotoImage(file='chidouren.gif')
        image2 = canvas.create_image(12 + 20 * chidouren[0], 12 + 20 * chidouren[1], anchor='center', image=image_file2)
        player1 = player.points[0]
        image_file4 = tkinter.PhotoImage(file='player.gif')
        image4 = canvas.create_image(12 + 20 * player1[0], 12 + 20 * player1[1], anchor='center', image=image_file4)
        time.sleep(1)


def player_move():
    while 1:
        time.sleep(1)
        player.set_toward(fangxiang)
        player.action(ai, radblock, beans, wall)


def while1():
    while 1:
        global lock
        while ai.exchange:
            with lock:
                print(ai.exchange)
                canvas.delete(tkinter.ALL)
                # 背景图片
                # image_file1 = tkinter.PhotoImage(file='002.gif')
                # image1 = canvas.create_image(option.size_x * 10, option.size_y * 10, anchor='center',image=image_file1)
                # 用图片放置墙
                douzi = beans.point3[0]
                image_file3 = tkinter.PhotoImage(file='douzi2.gif')
                image3 = canvas.create_image(12 + 20 * douzi[0], 12 + 20 * douzi[1], anchor='center', image=image_file3)
                image_file1 = tkinter.PhotoImage(file='qiang.gif')
                for i in wall.points1:
                    canvas.create_image(2 + 20 * i[0], 2 + 20 * i[1], anchor='nw', image=image_file1)
                for i in radblock.points2:
                    canvas.create_image(2 + 20 * i[0], 2 + 20 * i[1], anchor='nw', image=image_file1)
                # 加载画布
                canvas.pack()
                window.update()
                time.sleep(1.5)


thread = threading.Thread(target=aimove)
thread.name = "子线程1"
thread.start()
thread2 = threading.Thread(target=while1)
thread2.name = "子线程2"
thread2.start()
# thread3 = threading.Thread(target=player_move)
# thread3.name = "子线程3"
# thread3.start()

# 创建标签
l1 = tkinter.Label(window, bg='green', fg='white', width=25, height=1, text='您将与电脑一起比赛吃豆子')
l1.place(x=(1.5 * option.size_x), y=(20 * option.size_y + 5), anchor='nw')
l2 = tkinter.Label(window, bg='green', fg='white', width=25, height=1, text='比分')
l2.place(x=(1.5 * option.size_x), y=(20 * option.size_y + 45), anchor='nw')


def shang():
    global fangxiang
    fangxiang = 'shang'


def xia():
    global fangxiang
    fangxiang = 'xia'


def zuo():
    global fangxiang
    fangxiang = 'zuo'


def you():
    global fangxiang
    fangxiang = 'you'


# 放置按键
b1 = tkinter.Button(window, text='上', bg='yellow', fg='green', font=('blue', 12), width=10, height=2, command=shang)
b1.place(x=(14 * option.size_x), y=(20 * option.size_y + 10), anchor='nw')
b2 = tkinter.Button(window, text='下', bg='yellow', fg='green', font=('blue', 12), width=10, height=2, command=xia)
b2.place(x=(14 * option.size_x), y=(22 * option.size_y + 10), anchor='nw')
b3 = tkinter.Button(window, text='左', bg='yellow', fg='green', font=('blue', 12), width=10, height=2, command=zuo)
b3.place(x=(10 * option.size_x), y=(22 * option.size_y + 10), anchor='nw')
b4 = tkinter.Button(window, text='右', bg='yellow', fg='green', font=('blue', 12), width=10, height=2, command=you)
b4.place(x=(18 * option.size_x), y=(22 * option.size_y + 10), anchor='nw')

# 进入消息循环(显示窗口)


window.mainloop()


# 打包
'''
pyinstaller -F -w --icon=my.ico F:\exercise\pacman\tk.py -p (F:\exercise\pacman\ai.py, F:\exercise\pacman\displayer.py, F:\exercise\pacman\findway.py, F:\exercise\pacman\main.py, F:\exercise\pacman\option.py, F:\exercise\pacman\player.py, F:\exercise\pacman\randomwall.py, F:\exercise\pacman\001.gif, F:\exercise\pacman\002.gif, F:\exercise\pacman\chidouren.gif, F:\exercise\pacman\douzi2.gif, F:\exercise\pacman\player.gif, F:\exercise\pacman\qiang.gif)
'''
