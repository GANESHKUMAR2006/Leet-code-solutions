class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if sorted(set(str1))==sorted(set(str2)):
            return ''.join(sorted(set(min(str1,str2))))
        else:
            return ""