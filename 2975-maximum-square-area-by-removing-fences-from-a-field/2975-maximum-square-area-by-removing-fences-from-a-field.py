class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hashset=set()
        hfen=sorted(hFences+[1,m])
        vfen=sorted(vFences+[1,n])
        for i in range(len(hfen)):
            for j in range(i+1,len(hfen)):
                hashset.add(hfen[j]-hfen[i])
        ans=-1
        for i in range(len(vfen)):
            for j in range(i+1,len(vfen)):
                v=vfen[j]-vfen[i]
                if v in hashset:
                    ans=max(ans,v)
        if ans==-1:
            return -1
        return ans*ans%(10**9+7)