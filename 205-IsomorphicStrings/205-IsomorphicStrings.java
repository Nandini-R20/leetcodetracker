// Last updated: 8/11/2026, 12:24:33 PM
class Solution {
    public boolean isIsomorphic(String s, String t) {
        char arr1[]=s.toCharArray();
        char arr2[]=t.toCharArray();
        for(int i =0;i<arr1.length;i++){
            char ch1=arr1[i];
            char ch2=arr2[i];
            int count1=0;
            int count2=0;
            for(int j=i+1;j<arr1.length;j++){
                if(ch1==arr1[j])
                count1++;
                if(ch2==arr2[j])
                count2++;
                if(count1!=count2)
                return false;
            }
           
        }
         return true;
        
    }
}