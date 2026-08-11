// Last updated: 8/11/2026, 12:21:24 PM
class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count =0;
        for(String s: words){
            boolean isconsistent=true;
            for(char c:s.toCharArray()){
                if(!allowed.contains(s.valueOf(c))){
                    isconsistent =false;
                    break;
                }
            }
            if(isconsistent){
                count++;

            }
        }return count;
        
    }
}