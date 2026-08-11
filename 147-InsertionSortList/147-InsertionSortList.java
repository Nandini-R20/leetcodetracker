// Last updated: 8/11/2026, 12:24:58 PM
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
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode d = new ListNode(0); // Dummy node

        while (head != null) {
            ListNode next = head.next;

            // Use a temporary pointer starting from dummy
            ListNode temp = d;

            // Find the correct position to insert
            while (temp.next != null && temp.next.val < head.val) {
                temp = temp.next;
            }

            // Insert the node
            head.next = temp.next;
            temp.next = head;

            // Move to the next node
            head = next;
        }

        return d.next;
    }
}