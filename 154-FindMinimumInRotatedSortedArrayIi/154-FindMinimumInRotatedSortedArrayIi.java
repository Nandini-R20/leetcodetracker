// Last updated: 8/11/2026, 12:24:52 PM
class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        return nums[0];
    }
}