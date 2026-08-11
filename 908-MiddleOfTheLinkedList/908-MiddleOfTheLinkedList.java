// Last updated: 8/11/2026, 12:22:08 PM
 class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode t1=head,t2=head;
        while(t2!=null && t2.next!=null){
            t1=t1.next;
            t2=t2.next.next;
        }
        return t1;
    }
 }
      