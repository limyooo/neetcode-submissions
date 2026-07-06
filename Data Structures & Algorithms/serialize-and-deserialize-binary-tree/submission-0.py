# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + "," + left + "," + right
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        sp = data.split(',')
        self.index = 0
        def dfs():
            if sp[self.index] == "null":
                self.index += 1
                return None
            root = TreeNode(sp[self.index])
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
            