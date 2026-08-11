// Last updated: 8/11/2026, 12:20:33 PM
class Solution {
    public String triangleType(int[] nums) {
        int n = nums[0];
        int m = nums[1];
        int s = nums[2];
if(n+m<=s || n+s<=m || m+s<=n){
    return "none";
}
        if (n == m && m == s) {
            return "equilateral";
        } else if (n == m || m == s || n == s) {
            return "isosceles";
        } 
        else {
            return "scalene";
    
           
        }
    }
}