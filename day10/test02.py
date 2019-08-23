import pygame
import enum
import random
import math


@enum.unique
class Color(enum.Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)


class Boll(object):
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self._x = x
        self._y = y
        self._radius = radius
        self._sx = sx
        self._sy = sy
        self._color = color
        self._alive = True

    def move(self, screen):
        self._x += self._sx
        self._y += self._sy
        if self._x - self._radius <= 0 or self._x + self._radius >= screen.get_width():
            self._x = -self._sx
        if self._y - self._radius <= 0 or self._y + self._radius >= screen.get_height():
            self._y = -self._sy

    def eat(self, other):
        if self._alive and other._alive and self != other:
            dx = self._x - other._x
            dy = self._y - other._y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < self._radius + other._radius and self._radius > other._radius:
                other._alive = False
                self._radius = self._radius + int(other._radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self._color, (self._x, self._y), self._radius, 0)


def main():
    # 定义用来装所有球的容器
    bolls = []

    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption("大球吃小球")
    # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    # screen.fill((242, 242, 242))
    # # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    # pygame.draw.circle(screen, (255, 0, 0,), (100, 100), 30, 0)
    # # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    # pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = random.randint(10, 100)
                sx, sy = random.randint(-10, 10), random.randint(-10, 10)
                color = Color.random_color()
                boll = Boll(x, y, radius, sx, sy, color)
                bolls.append(boll)
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        for boll in bolls:
            if boll._alive:
                boll.draw(screen)
            else:
                bolls.remove(boll)

        pygame.display.flip()
        pygame.time.delay(50)
        for boll in bolls:
            boll.move(screen)
            for other in bolls:
                boll.eat(other)


if __name__ == '__main__':
    main()
