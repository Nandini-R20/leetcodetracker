// Last updated: 8/11/2026, 12:25:09 PM
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            
            if (fast == slow) {
                return true;
            }
        }

        return false;        
    }
}