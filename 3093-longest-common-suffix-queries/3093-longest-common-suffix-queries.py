class TrieNode:
    def __init__(self):
        self.child={}
        self.idx=-1
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie=TrieNode()
        def update(node,i):
            if node.idx==-1:
                node.idx=i
                return
            prev=node.idx
            if len(wordsContainer[i])<len(wordsContainer[prev]):
                node.idx=i
            elif len(wordsContainer[i])==len(wordsContainer[prev]):
                if i<prev:
                    node.idx=i
        for i,word in enumerate(wordsContainer):
            node=trie
            update(node,i)
            for ch in reversed(word):
                if ch not in node.child:
                    node.child[ch]=TrieNode()
                node=node.child[ch]
                update(node,i)
        ans=[]
        for query in wordsQuery:
            node=trie
            for ch in reversed(query):
                if ch not in node.child:
                    break
                node=node.child[ch]
            ans.append(node.idx)
        return ans
