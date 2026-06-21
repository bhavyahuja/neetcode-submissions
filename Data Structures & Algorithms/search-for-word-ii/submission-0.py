class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
        self.word=""

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        node=self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node=node.children[c]
        node.word=word
        node.end=True
    
    def search(self,word):
        node=self.root
        for c in word:
            if c not in node.children:
                return False
            node=node.children[c]
        return node.end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = set()
        ans=set()
        trie=Trie()
        for c in words:
            trie.insert(c)
        def dfs(r,c,node):
            if r<len(board) and r>=0 and c<len(board[0]) and c>=0 and (r,c) not in visited:
                char = board[r][c]
                if char not in node.children:
                    return
                node=node.children[char]
                if node.end:
                    ans.add(node.word)
                visited.add((r,c))
                dfs(r+1,c,node)
                dfs(r-1,c,node)
                dfs(r,c+1,node)
                dfs(r,c-1,node)
                visited.remove((r,c))
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, trie.root)
        return list(ans)





