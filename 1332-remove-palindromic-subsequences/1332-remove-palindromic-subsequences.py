class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s[::-1]==s:
            return 1
        hashset=set()
        for i in s:
            hashset.add(i)
        return len(hashset)