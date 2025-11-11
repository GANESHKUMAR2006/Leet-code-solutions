class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        new=''
        for i in words:
            new+=i
            if new==s:
                return True
        return False