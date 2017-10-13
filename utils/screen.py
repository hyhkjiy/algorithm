# -*- coding:utf-8 -*-
"""
对asciimatics的封装和使用
asciimatics项目地址：https://github.com/peterbrittain/asciimatics
asciimatics文档地址：http://asciimatics.readthedocs.io/en/stable/
"""
import time
import mock
from asciimatics.screen import Screen


class COLOR(object):
    BLACK = Screen.COLOUR_BLACK
    RED = Screen.COLOUR_RED
    GREEN = Screen.COLOUR_GREEN
    YELLOW = Screen.COLOUR_YELLOW
    BLUE = Screen.COLOUR_BLUE
    MAGENTA = Screen.COLOUR_MAGENTA
    CYAN = Screen.COLOUR_CYAN
    WHITE = Screen.COLOUR_WHITE


class DrawArray(list):
    def __init__(self, *args, **kwargs):
        super(DrawArray, self).__init__(*args, **kwargs)
        self.interval = 0.5  # 绘画间隔时间，以秒为单位
        self.history = []
        self.su = ScreenUtil()

    def __setitem__(self, key, value):
        if len(self.history) % 2 == 0:
            especial = len(self.history) and {self.history[-1]: COLOR.RED} or {}
            especial.update({key: COLOR.YELLOW})
            self.su.draw_int_array(self, especial=especial, seconds=self.interval)
        self.history.append(key)
        super(DrawArray, self).__setitem__(key, value)


class ScreenUtil:
    def clear(self):
        """
        asciimatics.screen.Screen.clear()方法偶尔会闪屏，不知道为什么。
        如果你知道原因，请通过email联系我：2632790902@qq.com
        """
        for row in range(self.screen.height):
            self.screen.move(0, row)
            self.screen.draw(self.screen.width, row, char=' ', colour=7, bg=0)

    def draw_int_array(self, array, especial=None, default_color=COLOR.WHITE, seconds=0.5):
        """
        将int类型数组渲染到控制台友好展示
        :param array: 要展示的数组
        :param especial:
            特殊列索引，渲染数组时特殊列颜色与普通列不一样。
            渲染时不会对参数内的索引进行检查，若索引不在array中，则不渲染，且不会抛出任何异常。
            参数类型为数组时默认渲染为ORDER.RED色，如：
            [1, 3, 8, ...]
            若要指定颜色，需要传入类似以下字典：
            {
                1: COLOR.RED,
                2: COLOR.YELLOW,
                ...
            }
        :param default_color: 渲染颜色，默认为COLOR.WHITE
        :param seconds: 保持时间，默认保持0.5秒
        """
        if len(filter(lambda obj: isinstance(obj, int), array)) < len(array):  # 不是int类型数组的时候不做任何操作
            return
        if isinstance(especial, list):
            especial = {i: COLOR.RED for i in especial}
        for i, number in enumerate(array):
            self.screen.move(i, 0)
            if especial and i in especial:
                self.screen.draw(i, number, char='#', colour=especial[i])
            else:
                self.screen.draw(i, number, char='#', colour=default_color)
        self.screen.refresh()
        time.sleep(seconds)
        self.clear()

    @staticmethod
    def open(*args, **kwargs):
        return Screen.open(*args, **kwargs)

    def __init__(self, screen=None, **kwargs):
        self.screen = screen or Screen.open(**kwargs)
        self.screen.refresh()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.screen.close()

    def close(self, *args, **kwargs):
        self.screen.close(*args, **kwargs)


def draw_sorting(sort, start=1, stop=31, interval=0.5):
    """
    绘制排序过程
    :param sort: 排序方法
    :param start: 起始数字
    :param stop: 结束数字 + 1
    :param interval: 绘画时间间隔
    """
    array = DrawArray(mock.sample_range(start, stop))
    try:
        array.interval = interval
        sort(array)
    finally:
        array.su.close()


def print_array(array, msg=None):
    """
    迭代输出一个可迭代对象（如列表）
    """
    assert hasattr(array, '__iter__'), '请传入一个可迭代对象'
    if msg:
        print msg.center(30, '=')
    for e in array:
        if isinstance(array, dict):
            print '%s: %s' % (e, array[e])
            continue
        print e


if __name__ == '__main__':
    print_array(mock.sample_exam_results(5))
