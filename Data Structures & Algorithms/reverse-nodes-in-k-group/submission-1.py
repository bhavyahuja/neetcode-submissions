# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        groupPrev=dummy

        while True:
            kth=self.getKth(groupPrev,k)
            if not kth:
                break
            groupNext=kth.next

            prev,curr=kth.next, groupPrev.next
            while curr!=groupNext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            tmp=groupPrev.next
            groupPrev.next=kth
            groupPrev=tmp
        return dummy.next
        
    def getKth(self, groupPrev,k):
        i=0
        while groupPrev and i<k:
            groupPrev=groupPrev.next
            i+=1
        if i<k:
            return None
        return groupPrev

                

