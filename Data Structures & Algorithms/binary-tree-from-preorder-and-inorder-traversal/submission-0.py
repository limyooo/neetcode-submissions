# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        mid = preorder[0]
        
        mid_index = inorder.index(mid)
        left_inorder = inorder[:mid_index]
        right_inorder = inorder[mid_index+1:]

        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]

        root = TreeNode(mid)
        root.left = self.buildTree(left_preorder,left_inorder)
        root.right = self.buildTree(right_preorder,right_inorder)
        return root



       