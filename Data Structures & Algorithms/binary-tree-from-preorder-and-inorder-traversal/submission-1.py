# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos={}
        for i,v in enumerate(inorder):
            pos[v]=i
        pre_idx=0
        def dfs(left, right):
            nonlocal pre_idx
            if left>right:
                return None
            
            root_val=preorder[pre_idx]
            pre_idx+=1

            root=TreeNode(root_val)
            idx=pos[root_val]

            root.left=dfs(left, idx-1)
            root.right=dfs(idx+1, right)
            return root
        return dfs(0, len(inorder)-1)