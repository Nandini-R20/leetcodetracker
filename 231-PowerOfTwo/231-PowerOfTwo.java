// Last updated: 8/11/2026, 12:24:18 PM

 class Solution {
    public static boolean isPowerOfTwo(int n) {
        if (n == 0) return false;
        if (n == 1) return true;
        if (n % 2!= 0) return false;
        return isPowerOfTwo(n / 2);
    }
 }
    