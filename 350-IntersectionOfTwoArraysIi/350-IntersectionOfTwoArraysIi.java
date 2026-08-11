// Last updated: 8/11/2026, 12:23:24 PM
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashSet<Integer> n = new HashSet<>();
        int[] temp = new int[Math.min(nums1.length, nums2.length)];
        int index = 0;
        for (int num : nums1) {
        n.add(num);
 }

for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                if (nums1[i] == nums2[j]) {
                    temp[index++] = nums1[i]; 
                    nums2[j] = -1; 
                    break;
                }
            }
        }
        int[] result = new int[index];
        for (int i = 0; i < index; i++) {
            result[i] = temp[i];
        }

        return result;
    }
}
