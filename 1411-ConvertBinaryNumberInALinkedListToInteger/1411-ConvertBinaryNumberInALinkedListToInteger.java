// Last updated: 8/11/2026, 12:21:41 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */


public class Solution {
    public int getDecimalValue(ListNode head) {
        int result = 0;
        
        while (head != null) {
            result = (result << 1) | head.val; // Shift left and add current bit
            head = head.next;
        }
        
        return result;
    }
}
