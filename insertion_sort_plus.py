# -*- coding:utf-8 -*-
from utils import mock, screen, used_time


def insertion_sort_plus(array):
    """
    插入排序优化版
    复杂度： O(n^2)
    思路：
        在插入时从后往前比较，若不是最终位置则向后复制一份当前比较位置的数据，而不是与排序值进行交换。
    """
    for index in xrange(1, len(array)):  # 遍历数组无序部分
        temp = array[index]  # 备份当前要插入的数据
        for j in reversed(xrange(index)):  # 倒序遍历数组有序部分
            if temp < array[j]:  # 判断当前元素是否大于有序部分的某一个元素
                array[j + 1] = array[j]  # index前比temp大的元素后移一位
                if j == 0:  # 如果已到达第一个元素，说明当前数据在有序部分最小，直接放在开始位置
                    array[0] = temp
                    break  # 插入完成后结束本次遍历
            else:  # 如果有序部分的一个数比要插入的数据小，就将要插入的数据排在他后面
                array[j + 1] = temp
                break  # 插入完成后结束本次遍历


if __name__ == '__main__':
    # 对算法进行可视化
    screen.draw_sorting(insertion_sort_plus, interval=1, frame_frequency=0.5, tag_num=1)

    # 对对象列表进行插入排序
    exam_results = mock.sample_exam_results(8)
    screen.print_array(exam_results, '排序前')
    insertion_sort_plus(exam_results)
    screen.print_array(exam_results, '排序后')

    # 测试用时
    print '排序10000个数字耗时：', used_time(insertion_sort_plus, num=10000)
