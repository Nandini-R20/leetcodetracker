// Last updated: 8/11/2026, 12:26:12 PM
class Solution {
    public int mySqrt(int x) {
        if (x == 0 || x == 1) return x;

        int i = 1;

        
        while ((long) i * i <= x) {
            if((i+1)*(i+1)>x){
                return i;
            }
            i++;
        }

        return i - 1;
    }
}
