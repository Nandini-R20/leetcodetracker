// Last updated: 8/11/2026, 12:22:57 PM
class Solution {
    public List<Integer> findAnagrams(String str, String anagram) {
                 ArrayList<Integer> list = new ArrayList<>();
        int n = anagram.length();
        for (int i = 0; i <= str.length() - n; i++) { 
            boolean x = isanagram(i, i + n, str, anagram);
            if (x) list.add(i);
        }
        return list;
    }
    static boolean isanagram(int start, int end, String str, String anagram) {
        int[] arr = new int[26];

        for (int i = 0; i < anagram.length(); i++) { 
            arr[anagram.charAt(i) - 'a']++;
        }
        for (int i = start; i < end; i++) {
            arr[str.charAt(i) - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (arr[i] != 0) return false;
        }
        return true;
    }
}