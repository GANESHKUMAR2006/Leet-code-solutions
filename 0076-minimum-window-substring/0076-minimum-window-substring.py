class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)==0:
            return ''
        from collections import Counter
        countT=Counter(t)
        word={}
        need=len(countT)
        have=0
        res=[-1,-1]
        reslen=float('inf')
        l=0
        for r in range(len(s)):
            word[s[r]]=word.get(s[r],0)+1
            if s[r] in countT and word[s[r]]==countT[s[r]]:
                have+=1
            while need==have:
                if r-l+1<reslen:
                    res=[l,r]
                    reslen=r-l+1
                word[s[l]]-=1
                if s[l] in countT and word[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float('inf') else ''