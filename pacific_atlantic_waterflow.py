class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights),len(heights[0])
        pacific,atlantic = set(),set()
        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if i==0 or j==0:
                    pacific.add((i,j))
                if i==ROWS-1 or j==COLS-1:
                    atlantic.add((i,j))
        
        direct = [[1,0],[-1,0],[0,1],[0,-1]]
        
        
        q = list(pacific)
        while q:
            r,c = q.pop(0)
            for [r1,c1] in direct:
                if 0<=r+r1<ROWS and 0<=c+c1<COLS and heights[r+r1][c+c1]>=heights[r][c] and (r+r1,c+c1) not in pacific:
                    pacific.add((r+r1,c+c1))
                    q.append((r+r1,c+c1))
        
        q = list(atlantic)
        while q:
            r,c = q.pop(0)
            for r1,c1 in direct:
                if 0<=r+r1<ROWS and 0<=c+c1<COLS and heights[r+r1][c+c1]>=heights[r][c] and (r+r1,c+c1) not in atlantic:
                    atlantic.add((r+r1,c+c1))
                    q.append((r+r1,c+c1))
        
      
        for (r,c) in pacific:
            if (r,c) in atlantic:
                result.append([r,c])
        return result
