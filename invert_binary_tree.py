# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        if not root or (not root.left and not root.right):
            return root
        
        if root.left:
            self.invertTree(root.left)
        
        if root.right:
            self.invertTree(root.right)
        
        root.left,root.right = root.right, root.left
        return root
            
        
