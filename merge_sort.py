# -*- coding:utf-8 -*-
from utils import screen, mock, used_time


def __merge(array, start, end, middle):
    index_left = start
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
    if array[middle - 1] <= array[middle]:  # 如果左边部分最后(最大)一个数小于右边部分最前(最小)一个数，则左右部分已经有序
        return
    __merge(array, start, end, middle)  # 归并左右部分


def merge_sort(array):
    """
    归并排序算法
    复杂度： log(n)
    思路：
        归并排序也是采用分组排序的方式，每次将两个有序的数组归并成一个有序数组，然后进行递归，直到只剩下一个数组的时候排序就完成了。

        8 5 2 0 1 6 3 9
        A A A A B B B B  # 将待排序的数组分为左右两组


        8 5 2 0 1 6 3 9
        A A A A B B B B
        a a b b c c d d  # 将每组继续分为左右两组


        8 5 2 0 1 6 3 9
        A A A A B B B B
        a a b b c c d d
        1 2 3 4 5 6 7 8  # 直至分到每组只有一个元素


        5 8 0 2 1 6 3 9  # 按最底层分组进行归并
        A A A A B B B B
        a a b b c c d d


        0 2 5 8 1 3 6 9  # 继续归并
        A A A A B B B B


        0 1 2 3 5 6 8 9  # 归并完最顶层的分组后，排序完成

    """

    __merge_sort(array, 0, len(array))


if __name__ == '__main__':
    # 对算法进行可视化
    screen.draw_sorting(merge_sort, interval=0.1)

    # 对对象列表进行选择排序
    exam_results = mock.sample_exam_results(9)
    screen.print_array(exam_results, '排序前')
    merge_sort(exam_results)
    screen.print_array(exam_results, '排序后')

    # 测试用时
    print '排序10000个数字耗时：', used_time(merge_sort, num=10000)
