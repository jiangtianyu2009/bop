from SortUtility import Sort
import random
import datetime


def test_sort_result():
    unsortedlist = []
    for i in range(20):
        unsortedlist.append(random.randint(1, 99))
    print(unsortedlist)
    list_bubble = unsortedlist
    list_quick = unsortedlist
    print(list_bubble)
    print(list_quick)
    # assert list_bubble == list_quick
    # Execute sort
    list_bubble_sorted = Sort().bubbleSort(list_bubble)
    print(list_bubble_sorted)
    list_quick_sorted = Sort().quickSort(list_quick)
    print(list_quick_sorted)
    # assert list_bubble_sorted == list_quick_sorted


if __name__ == "__main__":
    unsortedlist = []
    for i in range(20):
        unsortedlist.append(random.randint(1, 99))
    # Quick sort time cost
    quick_time_start = datetime.datetime.now()
    sortedlist = Sort().bubbleSort(unsortedlist)
    quick_time_end = datetime.datetime.now()
    quick_time_delta = quick_time_end - quick_time_start
    print(quick_time_delta.total_seconds())
