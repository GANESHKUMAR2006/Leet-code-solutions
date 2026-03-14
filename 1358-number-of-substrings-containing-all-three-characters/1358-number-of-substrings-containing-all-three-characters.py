class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last=[-1]*3
        cnt=0
        for i in range(len(s)):
            last[ord(s[i])-ord('a')]=i
            if last[0]!=-1 and last[1]!=-1 and last[2]!=-1:
                cnt+=1+min(last)
        return cnt