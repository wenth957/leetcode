import tkinter
import tkinter.messagebox
import pygame
from enum import Enum, unique
from math import sqrt
from random import randint

# GUI图形用户界面tkinter
# step1:导入需要的东西
# step2:创建一个顶层窗口对象承载GUI应用
# step3:添加GUI组件
# step4:通过GUI组件将这些功能组织起来
# step5:进入主事件循环mainloop()


def main():
    flag = True

    # 修改标签上的文字

    def change_label_text():
        nonlocal flag
        # 外部函数的局部变量
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        '''确认退出'''
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗？'):
            top.quit()

    top = tkinter.Tk()
    # 创建顶层窗口
    top.geometry('240x160')
    # 设置窗口大小
    top.title('小游戏')
    # 创建窗口标题
    label = tkinter.Label(top, text='Hello,world!', font='Afial -32', fg='red')
    # top 窗口名称（font字体名称，字体大小）fg字体颜色 bg背景色
    label.pack(expand=1)
    # 放置到窗口top中
    panel = tkinter.Frame(top)
    # 创建一个装按钮的容器
    # 创建两个按钮添加到panel中
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # panel添加到top中
    tkinter.mainloop()
    # 开启主事件循环
    # mainloop 一旦检测到时间如鼠标点击等就会执行GUI代码
    # 并且会循环会一直执行直到下一个时间发生


# if __name__ == '__main__':
#    main()
# pygame进行游戏开发


def main1():
    # 制作游戏窗口
    pygame.init()
    # 初始化pygame中的模块
    screen = pygame.display.set_mode((800, 600))
    # 设置游戏窗口大小
    pygame.display.set_caption('大球吃小球')
    # 设置标题
    screen.fill((242, 242, 242))
    # 设置窗口的背景色
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 绘制⚪在窗口上，颜色，圆心，半径，0表示填充圆
    pygame.display.flip()
    # 刷新当前窗口（将绘制的图像呈现出来）
    running = True
    # 开启事件循环处理发生的事件
    while running:
        for event in pygame.event.get():
            # 从消息队列中获取事件
            if event.type == pygame.QUIT:
                running = False


# if __name__ == '__main__':
#    main1()


def main2():
    pygame.init()
    # 初始化模块
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((255, 255, 255))
    # 填充背景色
    path = 'D:/vs_code_python/days_100/res/ball.png'
    ball_image = pygame.image.load(path)
    # 加载图片变量
    screen.blit(ball_image, (50, 50))
    # 在窗口上渲染图像
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


# if __name__ == '__main__':
#     main2()
# 实现动画效果
# 将不连续的图片连续播放，每秒达到一定的帧数即可
# 每张图片不断改变球的位置即可


def main3():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    x, y = 50, 50
    # 小球坐标
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        # 每个事件画一次球
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        pygame.time.delay(50)
        # 间隔50ms
        x, y = x + 5, y + 5


# if __name__ == '__main__':
#    main3()
# 碰撞检测：sprite模块
# 检测两个球有没有碰撞:球心距小于半径之和
# 通过鼠标事件创造颜色、大小、移动速度随机的小球


@unique
class Color(Enum):
    # 枚举类
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        '''获取随机颜色'''
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    '''球'''
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        '''移动'''
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            # 不能显示整个圆
            self.sx = -self.sx
            # 反向移动
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        '''吃其他球'''
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx**2 + dy**2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)
                # 变大

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius,
                           0)


# 事件处理


def main4():
    balls = []
    # 所有球的容器
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN and \
                    event.button == 1:
                x, y = event.pos
                # 获取鼠标位置
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                # 在鼠标位置创建一个球
                balls.append(ball)
            screen.fill((255, 255, 255))
            # 取出容器里的球，没有被吃掉绘制，吃掉移除
            for ball in balls:
                if ball.alive:
                    ball.draw(screen)
                else:
                    balls.remove(ball)
            pygame.display.flip()
            pygame.time.delay(50)
            for ball in balls:
                ball.move(screen)
                for other in balls:
                    ball.eat(other)
                # 是否吃到了其他球


if __name__ == '__main__':
    main4()
