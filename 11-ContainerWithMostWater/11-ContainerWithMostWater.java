// Last updated: 8/11/2026, 12:27:30 PM
class Solution {
    public int maxArea(int[] arr) {
        int left = 0;
        int right = arr.length - 1;
        int maxArea = 0;

        while (left < right) {
            int minHeight = Math.min(arr[left], arr[right]);
            int length = right - left;
            int area = length * minHeight;

          
            if (area > maxArea) {
                maxArea = area;
            }

            if (arr[left] < arr[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
