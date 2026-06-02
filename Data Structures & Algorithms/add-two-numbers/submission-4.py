# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum=0
        cur=l1
        i=1
        while cur:
            sum+=cur.val*i
            i=i*10
            cur=cur.next
        cur=l2
        i=1
        while cur:
            sum+=cur.val*i
            i=i*10
            cur=cur.next
        if sum==0:
            return ListNode(0)
        ans=ListNode()
        cur=ans
        while sum>0:
            n=sum%10
            sum//=10
            cur.next=ListNode(n)
            cur=cur.next
        return ans.next