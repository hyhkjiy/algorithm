# -*- coding:utf-8 -*-
from utils import mock, screen, used_time


def selection_sort(array):
    """
    选择排序算法
    复杂度： O(n^2)
    思路：
        遍历数组，在遍历过程中按索引从小到大依次排序，每次排序将从没有排序的部分取中出最小值与当前应排序位置数据进行交换。
    """
    for index in xrange(len(array)):  # 遍历数组
        min_index = index  # 存储每一轮排序的最小值
        for j in xrange(index, len(array)):  # 遍历未排序部分
            if array[j] < array[min_index]:  # 找出未排序部分最小值
                min_index = j
        array[min_index], array[index] = array[index], array[min_index]  # 将最小值与排序位置值进行交换


if __name__ == '__main__':
    # 对算法进行可视化
    screen.draw_sorting(selection_sort)

    # 对对象列表进行选择排序
    exam_results = mock.sample_exam_results(80)
    screen.print_array(exam_results, '排序前')
    selection_sort(exam_results)
    screen.print_array(exam_results, '排序后')

    # 测试用时
    print '排序10000个数字耗时：', used_time(selection_sort, num=10000)
