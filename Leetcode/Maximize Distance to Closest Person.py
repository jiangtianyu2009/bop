class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        seatcounter = 0
        maxseatcounter = 0
        for seat in seats:
            if seat is 0:
                seatcounter = seatcounter + 1
            else:
                if seatcounter > maxseatcounter:
                    maxseatcounter = seatcounter
                seatcounter = 0
        dist = maxseatcounter // 2 + maxseatcounter % 2

        seatcounter = 0
        maxseatcounter = 0
        isfirstone = 1
        if seats[0] is 0:
            for seat in seats:
                if seat is 0:
                    seatcounter = seatcounter + 1
                else:
                    if isfirstone is 1:
                        maxseatcounter = seatcounter
                        isfirstone = 0
        if maxseatcounter > dist:
            dist = maxseatcounter

        seatcounter = 0
        maxseatcounter = 0
        isfirstone = 1
        if seats[-1] is 0:
            seats = seats[::-1]
            for seat in seats:
                if seat is 0:
                    seatcounter = seatcounter + 1
                else:
                    if isfirstone is 1:
                        maxseatcounter = seatcounter
                        isfirstone = 0
        if maxseatcounter > dist:
            dist = maxseatcounter

        return dist


if __name__ == '__main__':
    listseat = [0, 1, 0, 1, 0]
    print(Solution().maxDistToClosest(listseat))
