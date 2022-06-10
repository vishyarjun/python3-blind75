"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        hsh = {}
        root = node
        q = [node]
        while q:
            curr = q.pop(0)
            if curr.val not in hsh:
                hsh[curr.val]  = Node(curr.val)
            root = hsh[curr.val]
            for neighbor in curr.neighbors:
                if neighbor.val not in hsh: 
                    hsh[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                root.neighbors.append(hsh[neighbor.val])
        return hsh[node.val]
