# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=1
        cur=head
        prev=None
        len=0
        while cur:
            len+=1
            cur=cur.next
        n=len-n
        cur=head
        print(n)
        if n==0:
            head=head.next
        while cur:
            prev=cur
            cur=cur.next
            if n==i:
                prev.next=cur.next
                if cur.next:
                    cur.next=cur.next.next
                else:
                    cur.next=None
            i+=1
        return head