// Last updated: 8/11/2026, 12:26:04 PM
class Solution {
    public void sortColors(int[] nums) {  
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = 0; j < nums.length - 1 - i; j++) {
                if (nums[j] > nums[j + 1]) {
                    int t = nums[j+1];
                    nums[j+1] = nums[j];
                    nums[j ] = t;
                }
            }
        }
            
            System.out.println(Arrays.toString(nums));
        
    }
}
        
    