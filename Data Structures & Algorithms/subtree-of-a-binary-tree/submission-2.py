# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def Same(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return Same(p.left,q.left) and Same(p.right,q.right)
        if not root:
            return False
        return Same(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            