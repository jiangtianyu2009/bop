public class Solution {
    public int HammingDistance(int x, int y) {
        int d = x ^ y;
        int counter = 0;
        while (d != 0) {
            if ((d >> 1) * 2 != d) {
                counter++;
            }
            d = d >> 1;
        }
        return counter;
    }
}