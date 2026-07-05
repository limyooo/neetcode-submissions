# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = deque([root])
        ans = []

        def bfs():
            while que:
                level_size = len(que)
                last_val = None
                for _ in range(level_size):
                    curr = que.popleft()
                    last_val = curr.val
                    if curr.left:
                        que.append(curr.left)
                    if curr.right:
                        que.append(curr.right)
                ans.append(last_val)
        bfs()
        return ans