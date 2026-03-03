class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashset=set()
        for ch in s:
            if ch in hashset:
                return ch
            hashset.add(ch)
        return ""