# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        return self.divide(lists, 0, len(lists)-1)
    
    def divide(self, lists, l, r):
        if l> r:
            return None
        if l==r:
            return lists[l]
        mid=(l+r)//2
        left=self.divide(lists, l, mid)
        right=self.divide(lists, mid+1, r)
        return self.conquer(left, right)
    
    def conquer(self, left, right):
        dummy=ListNode()
        cur=dummy
        while left and right:
            if left.val>right.val:
                cur.next=right
                right=right.next
                cur=cur.next
            else:
                cur.next=left
                left=left.next
                cur=cur.next
        if left:
            cur.next=left
        if right:
            cur.next=right
        return dummy.next
        