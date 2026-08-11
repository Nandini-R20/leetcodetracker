// Last updated: 8/11/2026, 12:26:43 PM
class Solution {
    public String countAndSay(int n) {
        String str="1";
       if(n==1){
        return str;
       }
       else{
        while(n>1){
        StringBuilder ans=new StringBuilder();
        int c=1,i=1;
        for(i=1;i<str.length();i++){
            if(str.charAt(i)==str.charAt(i-1))
               c++;
            else{
                ans.append(c).append(str.charAt(i-1));
                c=1;
            }
        }
        ans.append(c).append(str.charAt(i-1));
        str=ans.toString();
        n--;
        }
        
       }
       return str;
    }
}