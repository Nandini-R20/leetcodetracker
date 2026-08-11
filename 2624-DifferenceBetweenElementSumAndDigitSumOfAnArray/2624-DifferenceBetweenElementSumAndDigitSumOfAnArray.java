// Last updated: 8/11/2026, 12:20:42 PM
class Solution {
    public int differenceOfSum(int[] nums) {
        int sum=0,digit=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
            int n=nums[i];
            while(n!=0){
                digit+=(n%10);
                n/=10;
            }
        }

return Math.abs(sum-digit);        
    }
}