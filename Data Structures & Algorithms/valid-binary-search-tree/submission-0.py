# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.min_val = float('-inf')
        def dfs(node):
            if not node:
                return True
            if not dfs(node.left):
                return False
            if node.val > self.min_val:
                self.min_val = node.val
            else:
                return False
            return dfs(node.right)
        return dfs(root)