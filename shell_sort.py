# -*- coding:utf-8 -*-
from utils import mock, screen, used_time


def _selection_sort(array):
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


def _insertion_sort(array):
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


def shell_sort(array):
    """
    希尔排序算法
    复杂度： TODO
    思路：
        将无序数组分割为若干个子序列，子序列不是逐段分割的，而是相隔特定的增量的子序列，对各个子序列进行插入排序；
        然后再选择一个更小的增量，再将数组分割为多个子序列进行排序......
        最后选择增量为1，即使用直接插入排序，使最终数组成为有序。
        例如：
        8 5 2 0 1 6 3 9
        a b c d a b c d  第一轮增量为4，索引为0的"8"和索引为0+4的"1"同时被分到a组进行插入排序，
                         索引为1的"5"，和索引为1+4的"6"同时被分到b组进行排序，c、d组同理，排序后写入回原数组对应位置。

        1 5 2 0 8 6 3 9  第一轮结果
        a b a b a b a b  第二轮增量为2，索引为0+2*0的"1"、索引为0+2*1的"2"、索引为0+2*2的"8"、为0+2*3的"3"被分到a组进行插入排序，b组同理，排序后写回原数组对应位置。

        1 0 2 5 3 6 8 9  第二轮结果，可以看到a、b各组的数据已经有序(1 2 3 8, 0 5 6 9)
        a a a a a a a a  第三轮增量为1，所有位置的数据同时被分到a组进行插入排序，排序后写回数组对应位置，此时整个数组排序完成。

        0 1 2 3 5 6 8 9  第三轮后排序完成


    优化原理：
        根据上面的思路整理，发现第二轮排序后整个数组依然是乱序，第三轮步进为1的时候才有连续有序数组。
        那前面几步的排序工作是为了什么呢？
        这和插入排序的原理有关，在插入排序第二层循环内，如果在遍历完成之前成功找到元素位置就可以直接结束该次循环，进行下一个元素的插入。
        所以插入排序在对大致有序的数组排序时效率极高，极端情况下复杂度可以达到O(n)。
        为了发挥插入排序的优势，希尔排序每一轮将相隔一定位置的数据进行排序，间隔越小的时候数组越接近有序，插入排序的复杂度就越低。

    """
    interval = len(array) / 2  # 设置增量为数组长度除以2
    while True:
        for i in range(interval):  # 迭代增量次，得到每一轮的子序列
            sub_array = array[i::interval]  # 得到子序列
            _insertion_sort(sub_array)  # 用插入排序对子序列排序
            # _selection_sort(sub_array)  # 思考：如果此处的插入排序换成选择排序，效率会有什么影响呢？
            for n in range(len(sub_array)):  # 将排序后的子序列放回要排序数组
                array[i + n * interval] = sub_array[n]  # 将排序后的子序列放回要排序数组对应位置

        if interval == 1:  # 当增量为1时数组已经有序，退出循环
            break
        interval /= 2  # 每次增量除以2，直到增量为1


if __name__ == '__main__':
    # 对算法进行可视化
    screen.draw_sorting(shell_sort, interval=0.1, frame_frequency=1, tag_num=1)

    # 对对象列表进行希尔排序
    exam_results = mock.sample_exam_results(80)
    screen.print_array(exam_results, '排序前')
    shell_sort(exam_results)
    screen.print_array(exam_results, '排序后')

    # 测试用时
    print '排序10000个数字耗时：', used_time(shell_sort, num=10000)
    # 可以看出相对于插入排序，希尔排序提升了几十倍的效率
