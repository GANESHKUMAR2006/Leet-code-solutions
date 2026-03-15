class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict,Counter
        countT=Counter(t)
        need=len(countT)
        have=0
        mp={}
        left=0
        reslen=float('inf')
        res=[-1,-1]
        for right in range(len(s)):
            mp[s[right]]=mp.get(s[right],0)+1
            if s[right] in countT and mp[s[right]]==countT[s[right]]:
                have+=1
            while need==have:
                if right-left+1<reslen:
                    res=[left,right]
                    reslen=right-left+1
                mp[s[left]]-=1
                if s[left] in countT and mp[s[left]]<countT[s[left]]:
                    have-=1
                left+=1
        l,r=res
        return s[l:r+1] if reslen!=float('inf') else ""