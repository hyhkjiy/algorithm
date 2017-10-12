# -*- coding:utf-8 -*-
import random

from screen_util import ScreenProxy, COLOR

"""
选择排序算法
复杂度：TODO
思路：
    遍历数组，在遍历过程中按索引从小到大依次排序，每次排序将从没有排序的部分取中出最小值与当前应排序位置数据进行交换。
"""
# 产生随机数据
arr = range(1, 31)
random.shuffle(arr)

with ScreenProxy() as sp:
    screen = sp.screen
    for index in xrange(len(arr)):  # 遍历数组
        min_index = index  # 存储每一轮排序的最小值
        for j in xrange(index, len(arr)):  # 遍历未排序部分
            if arr[j] < arr[min_index]:  # 找出未排序部分最小值
                min_index = j

        # 可视化代码（可忽略）
        sp.clear()
        especial = {i: COLOR.GREEN for i in range(index)}
        especial.update({min_index: COLOR.YELLOW, index: COLOR.RED})
        sp.draw_int_array(arr, especial=especial)
        screen.refresh()
        sp.sleep(0.5)

        arr[min_index], arr[index] = arr[index], arr[min_index]  # 将最小值与排序位置值进行交换
