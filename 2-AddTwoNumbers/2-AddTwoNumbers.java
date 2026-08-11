// Last updated: 8/11/2026, 12:27:47 PM
// Definition for singly-linked list.
// public class ListNode {
//     int val;
//     ListNode next;
//     ListNode() {}
//     ListNode(int val) { this.val = val; }
//     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
//}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head= new ListNode(-1);
        ListNode temp = head;
        int c = 0;
        while (l1 != null || l2 != null || c != 0) {
            int x= (l1 != null )? l1.val:0;
            int y=  (l2 != null )? l2.val:0;
            int sum=x+y+c;
            temp.next=new ListNode(sum%10);
            c=sum/10;
            temp=temp.next;
            if(l1!=null)l1=l1.next;
           if(l2!=null)l2=l2.next;
        }
        return head.next;
    }
}