class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        for i in range(0,len(sentence)):
            if searchWord==sentence[i][:len(searchWord)]:
                return i+1
                break
        return -1