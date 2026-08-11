// Last updated: 8/11/2026, 12:23:54 PM
class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
        int total=(n*(n+1))/2;
        int sum=0;
        for(int k:nums){
            sum+=k;
        }
        int mis=total-sum;
        return mis;
        }
    
}