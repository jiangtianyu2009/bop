class Sort:
    def quickSort(self, unsortedlist):
        if len(unsortedlist) <= 1:
            return unsortedlist
        pivot = unsortedlist[0]
        unsortedlist.remove(unsortedlist[0])
        left, right = [], []
        for num in unsortedlist:
            if num < pivot:
                left.append(num)
            else:
                right.append(num)
        return self.quickSort(left) + [pivot] + self.quickSort(right)


if __name__ == "__main__":
    a = [76, 76, 65, 72, 58, 64, 82, 3, 22, 31]
    print(Sort().quickSort(a))
    print(Sort().quickSort(a))
    print(Sort().quickSort(a))
