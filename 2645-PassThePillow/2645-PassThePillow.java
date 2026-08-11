// Last updated: 8/11/2026, 12:20:29 PM
class Solution {
    public int passThePillow(int n, int time) {
        int turn=((n-1)*2);
        time%=turn;
        if(time<n) return time+1;
        return(turn-time+1);
        
    }
}