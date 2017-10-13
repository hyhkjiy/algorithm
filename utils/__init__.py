# -*- coding:utf-8 -*-
from utils.mock import sample_range
import time


def used_time(sort, num=10000):
    sample_array = sample_range(num)
    start_time = time.time()
    sort(sample_array)
    return time.time() - start_time
