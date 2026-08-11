// Last updated: 8/11/2026, 12:23:33 PM
class Solution {
    public String reverseVowels(String s) {
        char[] arr=s.toCharArray();
        int l=0;
        int r=arr.length-1;
        while(l<r){
        while(l<r&& !isVowel(arr[l])){
            l++;
        }
        while(l<r&& !isVowel(arr[r])){
            r--;
        }
        char t=arr[l];
        arr[l]=arr[r];
        arr[r]=t;
        l++;
        r--;
    }
    return new String(arr);
    }
    public boolean isVowel(char c){
        return c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U';
    }
}