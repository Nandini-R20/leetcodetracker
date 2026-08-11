// Last updated: 8/11/2026, 12:27:39 PM
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] arr = merge(nums1 , nums2);
        int n = arr.length;
        double mid;
        if(n % 2 == 0){
            mid = (arr[(n / 2) - 1] + arr[(n / 2)]) / 2.0;
        }
        else{
            mid = arr[n / 2];
        }
        return mid;
    }
    public static int[] merge(int[] first, int[] second){
        int[] m = new int[first.length + second.length];
        int i = 0;
        int j = 0;
        int k = 0;
        while(i < first.length && j < second.length){
            if(first[i] < second[j]){
                m[k] = first[i];
                i++;
            }
            else{
                m[k] = second[j];
                j++;
            }
            k++;
        }
        while(i < first.length){
            m[k] = first[i];
            i++;
            k++;
        }
        while(j < second.length){
            m[k] = second[j];
            j++;
            k++;
        }
        return m;
    }
}