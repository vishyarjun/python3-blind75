class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:     
        ROWS =len(board)
        COLS = len(board[0])
        
        
        def dfs(r,c,word):
            if len(word)==0:
                return True
            if r<0 or r>=ROWS or c<0 or c>=COLS or board[r][c]!=word[0]:
                return
            dir = [[1,0],[-1,0],[0,1],[0,-1]]
            
            ch = board[r][c]
            board[r][c]='#'
            for d in dir:
                if dfs(r+d[0],c+d[1],word[1:]):
                    return True
            board[r][c] = ch
            
            
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]==word[0]:
                    res = dfs(i,j,word)
                    if res:
                        return True
        return False
