from SortUtility import Sort
import random
import datetime
import copy


def test_sort_result():
    unsortedlist = []
    for i in range(1000):
        unsortedlist.append(random.randint(1, 999))
    list_bubble = copy.deepcopy(unsortedlist)
    list_quick = copy.deepcopy(unsortedlist)
    print('list_bubble: ', list_bubble)
    print('list_quick : ', list_quick)
    # Execute sort
    list_bubble_sorted = Sort().bubbleSort(list_bubble)
    print('list_bubble_sorted: ', list_bubble_sorted)
    list_quick_sorted = Sort().quickSort(list_quick)
    print('list_quick_sorted : ', list_quick_sorted)
    assert list_quick_sorted == list_bubble_sorted


if __name__ == "__main__":
    test_sort_result()
    # unsortedlist = []
    # for i in range(20):
    #     unsortedlist.append(random.randint(1, 99))
    # # Quick sort time cost
    # quick_time_start = datetime.datetime.now()
    # sortedlist = Sort().bubbleSort(unsortedlist)
    # quick_time_end = datetime.datetime.now()
    # quick_time_delta = quick_time_end - quick_time_start
    # print(quick_time_delta.total_seconds())
