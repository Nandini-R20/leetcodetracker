// Last updated: 8/11/2026, 12:24:02 PM
class Solution {
    public int addDigits(int num ) {
        int sum=0;
        // if(num<0)
        // return 0;
        
        while(num>=10){
sum=0;

while(num>0){
    int d=num%10;
    sum+=d;

 num=num/10;
 
}num=sum;
        }
    return num;
    }
}