# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.que = deque([root])
        self.bfs(root,self.res,self.que)
        return self.res
    def bfs(self,node,res,que):
        
        while self.que:
            level_size = len(self.que)
            level_node = []
            for _ in range(level_size):
                curr = que.popleft()
                level_node.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            self.res.append(level_node)

