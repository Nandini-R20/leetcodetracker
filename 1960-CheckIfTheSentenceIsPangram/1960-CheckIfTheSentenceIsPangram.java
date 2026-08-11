// Last updated: 8/11/2026, 12:21:13 PM
class Solution {
    public boolean checkIfPangram(String sentence) {
        for(char i='a';i<='z';i++)
        {
            if(sentence.indexOf(i)==-1)
            {
                return false;
            }

        }
        return true;
        
    }
}