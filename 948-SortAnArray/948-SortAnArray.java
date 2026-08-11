// Last updated: 8/11/2026, 12:22:06 PM
class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums);
        return nums;
    }

    private void mergeSort(int[] a) {
        int n = a.length;
        if (n <= 1) return;

        int mid = n / 2;
        int[] leftarray = new int[mid];
        int[] rightarray = new int[n - mid];

        for (int i = 0; i < mid; i++) {
            leftarray[i] = a[i];
        }


        for (int i = mid; i < n; i++) {
            rightarray[i - mid] = a[i];
        }

        mergeSort(leftarray);
        mergeSort(rightarray);
        merge(leftarray, rightarray, a);
    }

    private void merge(int[] leftarray, int[] rightarray, int[] a) {
        int i = 0, le = 0, ri = 0;
        int lesize = leftarray.length;
        int risize = rightarray.length;

        while (le < lesize && ri < risize) {
            if (leftarray[le] < rightarray[ri]) {
                a[i++] = leftarray[le++];
            } else {
                a[i++] = rightarray[ri++];
            }
        }

        while (le < lesize) {
            a[i++] = leftarray[le++];
        }

        while (ri < risize) {
            a[i++] = rightarray[ri++];
        }
    }
}