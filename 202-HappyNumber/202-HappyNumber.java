// Last updated: 8/11/2026, 12:24:36 PM
class Solution {

    public boolean isHappy(int n) {

        while (n != 1 && n != 4) {
            n = myFormula(n);
        }

        return n == 1;
    }

    public int myFormula(int n) {

        int sum = 0;

        while (n > 0) {

            int digit = n % 10;

            sum += digit * digit;

            n = n / 10;
        }

        return sum;
    }
}