# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        print(arr)
        i=0
        while i+k<=len(arr):
            arr[i:i+k]=reversed(arr[i:i+k])
            i+=k
        print(arr)
        dummy=ListNode()
        cur=dummy
        i=0
        for x in arr:
            cur.next = ListNode(x)
            cur = cur.next

        return dummy.next