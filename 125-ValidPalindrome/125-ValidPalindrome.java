// Last updated: 8/11/2026, 12:25:18 PM
class Solution {
    public  static   boolean isPalindrome(String s) {
   String n = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();

        
        int left = 0;
        int right = n.length() - 1;
        while (left < right) {
        if (n.charAt(left) != n.charAt(right)) {
           return false;
            }
            left++;
            right--;
        }

        return true;
    }
}

 




