"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp={None:None}
        old=head
        while old:
            mp[old]=Node(old.val)
            old=old.next
        old=head
        while old:
            mp[old].next=mp[old.next]
            mp[old].random=mp[old.random]
            old=old.next
        return mp[head]
