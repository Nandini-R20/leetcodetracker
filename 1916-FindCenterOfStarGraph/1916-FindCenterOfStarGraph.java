// Last updated: 8/11/2026, 12:21:21 PM
class Solution {
    public int findCenter(int[][] e) {
        return e[0][0]==e[1][0] ||e[0][0]==e[1][1]?e[0][0]:e[0][1];
    }
}