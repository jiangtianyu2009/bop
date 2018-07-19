class RangeEncoding():
    def minRanges(self, arr):
        counter = 1
        preitem = arr[0]
        for item in arr[1:]:
            if item - preitem > 1:
                counter = counter + 1
            preitem = item
        return counter
