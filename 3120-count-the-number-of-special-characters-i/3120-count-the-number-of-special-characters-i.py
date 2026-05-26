class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        for w in set(word):
            if w.islower() and w.upper() in set(word):
                count+=1
        return count