// Last updated: 8/11/2026, 12:21:35 PM
class Solution {
    public int maxVowels(String s, int k) {
        boolean[] isVowel = new boolean[26];  
        isVowel['a' - 'a'] = true;
        isVowel['e' - 'a'] = true;
        isVowel['i' - 'a'] = true;
        isVowel['o' - 'a'] = true;
        isVowel['u' - 'a'] = true;

        int count = 0, maxCount = 0;

     
        for (int i = 0; i < k; i++) {
            if (isVowel[s.charAt(i) - 'a']) count++;
        }
        maxCount = count;

        for (int i = k; i < s.length(); i++) {
            if (isVowel[s.charAt(i) - 'a']) count++;
            if (isVowel[s.charAt(i - k) - 'a']) count--;
            if (count > maxCount) maxCount = count;
           
            if (maxCount == k) return k;
        }

        return maxCount;
    }
}
