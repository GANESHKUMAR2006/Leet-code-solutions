class Solution:
    def longestBalanced(self, s: str) -> int:
        ans=0
        n=len(s)
        from collections import defaultdict
        for i in range(n):
            mp=defaultdict(int)
            for j in range(i,n):
                mp[s[j]]+=1
                if len(set(mp.values()))==1:
                    ans=max(ans,j-i+1)
        return ans