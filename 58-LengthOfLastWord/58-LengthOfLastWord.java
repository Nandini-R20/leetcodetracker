// Last updated: 8/11/2026, 12:26:31 PM
class Solution {
    public int lengthOfLastWord(String s) {
                s = s.trim();
        return s.length()-s.lastIndexOf(" ")-1;
    }
}