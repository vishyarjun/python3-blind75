# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # 1,2,N,N,3,4,N,N,5,N,N
    def serialize(self, root):
        arr = []
        def dfs(node):
            arr.append(str(node.val) if node else 'N')
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            
        
        dfs(root)
        #print(','.join(arr))
        return ','.join(arr)
        
                    
    def deserialize(self, data):
        arr = data.split(',')
        
        def dfs():
            val = arr.pop(0)
            if val!='N':
                node = TreeNode(int(val))
                node.left = dfs()
                node.right = dfs()
                return node
            
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
