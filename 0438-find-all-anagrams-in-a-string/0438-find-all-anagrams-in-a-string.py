class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        plen=len(p)
        from collections import defaultdict
        from collections import Counter
        count=Counter(p)
        ans=[]
        left=0
        mp=defaultdict(int)
        for i in range(len(s)):
            mp[s[i]]+=1
            if i-left+1>len(p):
                mp[s[left]]-=1
                if mp[s[left]]==0:
                    del mp[s[left]]
                left+=1
            if mp==count:
                ans.append(left)
        return ans
