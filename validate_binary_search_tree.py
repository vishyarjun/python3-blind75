class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def valid(node, left, right):
            
            if not node:
                return True
            #print(left,node.val,right)
            if node.val >= right or node.val <= left:
                return False
            
            return valid(node.left,left,node.val) and valid(node.right,node.val,right)
        
        
        return valid(root,float("-inf"),float("inf"))
