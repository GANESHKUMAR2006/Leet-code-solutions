class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n=len(s)
        first=[n]*26
        last=[-1]*26
        for i,ch in enumerate(s):
            x=ord(ch)-ord('a')
            first[x]=min(first[x],i)
            last[x]=i
        def intervals(start):
            x=ord(s[start])-ord('a')
            left=first[x]
            right=last[x]
            i=left
            while i<=right:
                y=ord(s[i])-ord('a')
                if first[y]<left:
                    return None
                right=max(right,last[y])
                i+=1
            return left,right
        interval=[]
        for c in range(26):
            if first[c]==n:
                continue
            inter=intervals(first[c])
            if inter is not None:
                interval.append(inter)
        interval.sort(key=lambda x:x[1])
        ans=[]
        end=-1
        for left,right in interval:
            if left>end:
                ans.append(s[left:right+1])
                end=right
        return ans