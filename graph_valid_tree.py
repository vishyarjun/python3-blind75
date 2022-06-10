from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hsh = collections.defaultdict(list)
        for e1,e2 in edges:
            hsh[e1].append(e2)
            hsh[e2].append(e1)
        visited = set()
    
        def dfs(curr,prev):
            if curr in visited:
                return False
            visited.add(curr)
            for neighbor in hsh[curr]:
                if neighbor!=prev:
                    if not dfs(neighbor,curr):
                        return False
            return True
    
        return dfs(0,-1) and len(visited)==n
