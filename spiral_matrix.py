class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        
        soln = []
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        idx = 0
        r,c = 0,0
        while len(soln)!=len(matrix)*len(matrix[0]):
            #print(idx)
            cdr,cdc = directions[idx][0],directions[idx][1] # 0,1
            while True:
                #print(r,c)
                if (r,c) not in visited:
                    visited.add((r,c))
                    soln.append(matrix[r][c])
                if r+cdr<0 or r+cdr>=len(matrix) or c+cdc<0 or c+cdc>=len(matrix[0]) or (r+cdr,c+cdc) in visited:
                    idx = 0 if idx>=3 else idx+1
                    break
                r+=cdr
                c+=cdc
            
        return soln
