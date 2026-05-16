class Solution:
    def maxRepeating(self, s: str, w: str) -> int:
        dp=[0]*(len(s)+1)
        for i in range(len(w),len(s)+1):
            if s[i-len(w):i]==w:
                dp[i]+=dp[i-len(w)]+1
        return max(dp)