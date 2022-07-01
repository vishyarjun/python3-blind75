class Trie:

    def __init__(self):
        self.children = {}
        self.isWord = False
        

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isWord = True
            
            
    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
