# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q = [root]
        out = []
        while len(q)>0:
            q_len=len(q)
            curr = []
            for i in range(q_len):
                node = q.pop(0)
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            out.append(curr)
        
        return out
