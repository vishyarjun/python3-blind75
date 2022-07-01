class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
    def insert(self,word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board),len(board[0])
        output = set()
        trie = TrieNode()
        for word in words:
            trie.insert(word)
            
        def dfs(r,c,node):
            if r<0 or r>=ROWS or c<0 or c>=COLS or board[r][c]=='#' or board[r][c] not in node.children:
                return
            ch =  board[r][c]
            new = node.children[ch]
            if new.word:
                output.add(new.word)
            board[r][c] = '#'
            dfs(r+1,c,new)
            dfs(r-1,c,new)
            dfs(r,c+1,new)
            dfs(r,c-1,new)
            
            board[r][c] = ch
            
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,trie)
        return list(output)
