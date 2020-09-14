from SortUtility import Sort
import random

if __name__ == "__main__":
    unsortedlist = []
    for i in range(40):
        unsortedlist.append(random.randint(1, 99))
    print(unsortedlist)
    sortedlist = Sort().bubbleSort(unsortedlist)
    print(sortedlist)
