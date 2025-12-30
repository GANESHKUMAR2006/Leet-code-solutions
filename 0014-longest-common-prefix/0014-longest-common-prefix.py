class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n=len(strs[0])
        for length in range(n):
            ch=strs[0][length]
            for word in strs:
                if length==len(word) or ch!=word[length]:
                    return strs[0][:length]
        return strs[0]