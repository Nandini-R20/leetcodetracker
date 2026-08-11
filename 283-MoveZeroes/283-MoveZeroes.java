// Last updated: 8/11/2026, 12:23:50 PM
class Solution {
    public void moveZeroes(int[] nums) {
        int count=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                count++;
            }
        }
        int temp[]=new int[nums.length];
        int j=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=0){
            temp[j++]=nums[i];
                   }
        }
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
            temp[j++]=nums[i];
                   }
    }
    for(int i=0;i<nums.length;i++){
        nums[i]=temp[i];
    }
    }
}
