// Last updated: 8/11/2026, 12:26:48 PM
class Solution {
    public int strStr(String haystack, String needle) {
       int needleLen = needle.length();
       int haystackLen = haystack.length();

       for(int i = 0; i < haystackLen; i++){
            String sub = haystack.substring(i, Math.min(i + needleLen, haystackLen));
            if(sub.equals(needle)){
                return i;
            }
       }
    
        return -1;
    }
}