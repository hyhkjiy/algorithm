# -*- coding:utf-8 -*-
from utils import mock, screen, used_time


def insertion_sort(array):
    """
    插入排序算法
    复杂度： O(n^2)
    思路：
        遍历数组无序部分(从n-1开始)，取出无序部分任意一个值，依次与有序部分各个值比较，放入合适位置。
    """
    for index in xrange(1, len(array)):  # 遍历数组无序部分
        for j in xrange(index):  # 遍历数组有序部分
            if array[index] < array[j]:
                array[j], array[index] = array[index], array[j]  # 如果当前要排序的值比有序部分值小，就交换位置


if __name__ == '__main__':
    # 对算法进行可视化
    screen.draw_sorting(insertion_sort, interval=0.1)

    # 对对象列表进行插入排序
    exam_results = mock.sample_exam_results(8)
    screen.print_array(exam_results, '排序前')
    insertion_sort(exam_results)
    screen.print_array(exam_results, '排序后')

    # 测试用时
    print '排序10000个数字耗时：', used_time(insertion_sort, num=10000)
