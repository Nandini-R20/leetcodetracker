// Last updated: 8/11/2026, 12:20:50 PM
class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long ans=0;
        long s=0;
        for(int num:nums){
            if(num==0){
                s++;
                ans+=s;
            }
            else{
                s=0;
            }
        }
        return ans;
        
    }
}