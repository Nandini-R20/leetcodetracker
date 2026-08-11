// Last updated: 8/11/2026, 12:20:47 PM


class Solution {
    public String[] sortPeople(String[] names, int[] h) {
        for (int i = 0; i < h.length - 1; i++) {
            for (int j = 0; j < h.length - 1 ; j++) {
                if (h[j] < h[j + 1]) {
                    int t = h[j];
                    h[j] = h[j + 1];
                    h[j + 1] = t;
                     String str = names[j];
                    names[j] = names[j + 1];
                    names[j + 1] = str;
                }
            }
        }

        return names;
    }
}