# -*- coding:utf-8 -*-
from utils import mock
from utils.mock import sample_range
from utils.screen import ScreenProxy, COLOR


def selection_sort(array):
    """
    选择排序算法
    复杂度：TODO
    思路：
        遍历数组，在遍历过程中按索引从小到大依次排序，每次排序将从没有排序的部分取中出最小值与当前应排序位置数据进行交换。
    """
    with ScreenProxy() as sp:
        for index in xrange(len(array)):  # 遍历数组
            min_index = index  # 存储每一轮排序的最小值
            for j in xrange(index, len(array)):  # 遍历未排序部分
                if array[j] < array[min_index]:  # 找出未排序部分最小值
                    min_index = j

            # 可视化代码（可忽略）
            especial = {i: COLOR.GREEN for i in range(index)}
            especial.update({min_index: COLOR.YELLOW, index: COLOR.RED})
            sp.draw_int_array(array, especial=especial)

            array[min_index], array[index] = array[index], array[min_index]  # 将最小值与排序位置值进行交换


if __name__ == '__main__':
    # 产生随机数据
    arr = sample_range(1, 31)

    # 对数字列表进行选择排序
    selection_sort(arr)

    # 对对象列表进行选择排序
    exam_results = mock.sample_exam_results(8)
    ScreenProxy.dump_array(exam_results, '排序前')
    selection_sort(exam_results)
    ScreenProxy.dump_array(exam_results, '排序后')
