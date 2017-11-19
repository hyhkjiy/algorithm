# -*- coding:utf-8 -*-
# from utils import mock, screen, used_time
from utils import screen, mock, used_time


def __merge(array, start, end):
    index_left = start
    middle = int(end / 2.0 + start / 2.0)
    index_right = middle

    temp_arr = []
    while True:
        if index_left >= middle and index_right >= end:  # 如果左右两组都遍历完了
            for temp_index, arr_index in enumerate(range(start, end)):
                array[arr_index] = temp_arr[temp_index]  # 将排序好的列表写回原列表的指定位置
            return  # 结束循环
        elif index_left >= middle:  # 如果左边遍历完了右边还有
            temp_arr.append(array[index_right])
            index_right += 1
        elif index_right >= end:  # 如果右边遍历完了左边还有
            temp_arr.append(array[index_left])
            index_left += 1
        else:  # 都没有遍历完
            temp_arr.append(min(array[index_left], array[index_right]))  # 取出两个列表最小值中的最小值
            if temp_arr[-1] == array[index_left]:  # 判断最小值是从哪个列表取出的
                index_left += 1
            else:
                index_right += 1


def __merge_sort(array, start, end):
    # 对array[start...end)进行排序
    if end <= start + 1:
        return

    middle = int(end / 2.0 + start / 2.0)  # 中间数，start与end的平均数，为避免两数之和超出int范围，所以先除再加

    __merge_sort(array, start, middle)  # 排序数组左边部分
    __merge_sort(array, middle, end)  # 排序数组右边部分
    __merge(array, start, end)  # 归并左右部分


def merge_sort(array):
    """
    归并排序算法
    复杂度： log(n)
    思路：
        归并排序也是采用分组排序的方式，每次将两个有序的数组归并成一个有序数组，然后进行递归，直到只剩下一个数组的时候排序就完成了。

        a b c d e f g h
        8 5 2 0 1 6 3 9  # 未经过排序的初始数组，每个元素可以看成一个有序数组，一共n个，此时只有连续长度为1的元素有序

        a a b b c c d d  # 将两个有序的数组归并为一个（原a，b两组归并成新的a组;原c，d组归并成新的b组...）
        5 8 0 2 1 6 3 9  # 归并后每组又是有序的了，此时连续长度为2的元素有序（比如a组的5,8;b组的0,2;c组的1,6;e组的3,9）

        a a a a b b b b  # 继续将两个有序的数组归并为一个（上一轮的a，b组归并成为新的a组）
        0 2 5 8 1 3 6 9  # 归并后连续长度为4的数组保持有序（a组的4个元素和b组的4个元素）

        a a a a a a a a  # 继续归并
        0 1 2 3 5 6 8 9  # 此时连续8（n=8）个元素保持有序，排序完成


    """

    __merge_sort(array, 0, len(array))


if __name__ == '__main__':
    # 对算法进行可视化
    screen.draw_sorting(merge_sort)

    # 对对象列表进行选择排序
    exam_results = mock.sample_exam_results(9)
    screen.print_array(exam_results, '排序前')
    merge_sort(exam_results)
    screen.print_array(exam_results, '排序后')

    # 测试用时
    print '排序10000个数字耗时：', used_time(merge_sort, num=10000)
