# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        i=0
        while fast:
            if i%2==0:
                fast=fast.next
            else:
                fast=fast.next
                slow=slow.next
            i+=1
            if slow is fast:
                return True
        return False