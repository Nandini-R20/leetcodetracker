// Last updated: 8/11/2026, 12:27:26 PM
class Solution {
   public static String intToRoman(int num) {
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] s = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
 StringBuilder sb=new StringBuilder();
 for(int i=0;i<values.length;i++){
    while(num>=values[i]){
        num-=values[i];
        sb.append(s[i]);
    }
 }
return sb.toString();
}
}