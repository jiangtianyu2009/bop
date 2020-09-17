from SortUtility import Sort
import random
import datetime

if __name__ == "__main__":
    unsortedlist = []
    for i in range(9999):
        unsortedlist.append(random.randint(1, 99999))
    # Quick sort time cost
    quick_time_start = datetime.datetime.now()
    sortedlist = Sort().quickSort(unsortedlist)
    quick_time_end = datetime.datetime.now()
    quick_time_delta = quick_time_end - quick_time_start
    print(quick_time_delta.total_seconds())
