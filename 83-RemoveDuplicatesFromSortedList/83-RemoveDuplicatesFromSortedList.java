// Last updated: 8/11/2026, 12:25:54 PM
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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode current = head;
        
        while (current != null && current.next != null) {
            if (current.val == current.next.val) {
                // Skip the duplicate
                current.next = current.next.next;
            } else {
                // Move to next node if no duplicate
                current = current.next;
            }
        }
        
        return head;
    }
}
