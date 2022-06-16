class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_val=0
        ans = None
    
        def inorder(node):
            nonlocal k_val, ans
            
            if node.left:
                inorder(node.left)
            k_val+=1
            if k_val==k:
                if not ans:
                    ans = node.val
                return
            if node.right:
                inorder(node.right)
        
        
        inorder(root)
        return ans
