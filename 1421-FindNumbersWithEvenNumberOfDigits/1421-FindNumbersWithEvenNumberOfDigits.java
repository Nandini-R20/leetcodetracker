// Last updated: 8/11/2026, 12:21:38 PM
class Solution {
    public int findNumbers(int[] n) {
        int evenDigitCount = 0;

        for (int num : n) {
            int count = 0;
            int temp = num;

            while (temp > 0) {
                temp /= 10;
                count++;
            }

            if (count % 2 == 0) {
                evenDigitCount++;
            }
        }

        return evenDigitCount;
    }
}