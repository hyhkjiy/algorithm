# -*- coding:utf-8 -*-
from utils import screen, mock, used_time

from merge_sort import __merge


def merge_sort(array):
    """
    自低向上的归并算法
    复杂度： log(n)
    思路：
        和自顶向下的排序思路基本相同，不同的是直接分出最底层的小组，再向上合并

        a b c d e f g h
        8 5 2 0 1 6 3 9  # 未经过排序的初始数组，每个元素可以看成一个有序数组，一共n个，此时只有连续长度为1的元素有序

        a a b b c c d d  # 将两个有序的数组归并为一个（原a，b两组归并成新的a组;原c，d组归并成新的b组...）
        5 8 0 2 1 6 3 9  # 归并后每组又是有序的了，此时连续长度为2的元素有序（比如a组的5,8;b组的0,2;c组的1,6;e组的3,9）

        a a a a b b b b  # 继续将两个有序的数组归并为一个（上一轮的a，b组归并成为新的a组）
        0 2 5 8 1 3 6 9  # 归并后连续长度为4的数组保持有序（a组的4个元素和b组的4个元素）

        a a a a a a a a  # 继续归并
        0 1 2 3 5 6 8 9  # 此时连续8（n=8）个元素保持有序，排序完成

    """

    group_len = 2
    while True:
        for index in range((len(array) - 1) / group_len + 1):
            start = index * group_len
            end = min((index + 1) * group_len, len(array))
            __merge(array, start, end, start + min(group_len / 2, end - start))

        if group_len >= len(array):
            return

        group_len *= 2


if __name__ == '__main__':
    # 对算法进行可视化
    screen.draw_sorting(merge_sort, interval=0.1)
    #
    # # 对对象列表进行选择排序
    exam_results = mock.sample_exam_results(5)
    screen.print_array(exam_results, '排序前')
    merge_sort(exam_results)
    screen.print_array(exam_results, '排序后')
    #
    # # 测试用时
    print '排序10000个数字耗时：', used_time(merge_sort, num=10000)
