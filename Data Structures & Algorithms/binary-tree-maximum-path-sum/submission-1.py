# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
    
            path_sum = left+ right + node.val
            self.max_sum = max(path_sum,self.max_sum)
            return node.val + max(left , right) #最后一个node1也返回
        dfs(root)
        return self.max_sum