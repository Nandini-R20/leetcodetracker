// Last updated: 8/11/2026, 12:21:16 PM
class Solution {
    public int arraySign(int[] nums) {
    int c =0;
    for(int num:nums){
    if(num==0){
        return 0;
    }
    if(num<0){
       c++;
    }
    }
    return (c%2==0)?1:-1;
    }
}

 
