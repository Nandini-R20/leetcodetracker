// Last updated: 8/11/2026, 12:24:04 PM
class Solution {
    public boolean isAnagram(String s, String t) {
 char[] c1 = s.toCharArray();
        char[] c2 = t.toCharArray();   
        Arrays.sort(c1);
        Arrays.sort(c2);      
        return Arrays.equals(c1,c2);
    }
}   
        
    