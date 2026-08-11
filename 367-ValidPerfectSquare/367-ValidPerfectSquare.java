// Last updated: 8/11/2026, 12:23:21 PM

class Solution {
    public boolean isPerfectSquare(int num) {
        if (num < 1) return false; 

        for (int i = 1; i <= num / i; i++) {
            if (i * i == num) {
                return true;
            }
        }
        return false;
    }
}
