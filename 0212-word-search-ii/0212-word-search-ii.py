class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for word in words:
            node=root
            for ch in word:
                if ch not in node.children:
                    node.children[ch]=TrieNode()
                node=node.children[ch]
            node.word=word
        row=len(board)
        col=len(board[0])
        res=[]
        def dfs(r,c,node):
            ch=board[r][c]
            if ch not in node.children:
                return 
            nxt=node.children[ch]
            if nxt.word:
                res.append(nxt.word)
                nxt.word=None
            board[r][c]='#'
            for nr,nc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dr=r+nr
                dc=c+nc
                if (0<=dr<row and 0<=dc<col and board[dr][dc]!='#'):
                    dfs(dr,dc,nxt)
            board[r][c]=ch
        for r in range(row):
            for c in range(col):
                dfs(r,c,root)
        return res 