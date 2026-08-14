class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans=0
        from collections import defaultdict
        mp=defaultdict(int)
        left=0
        for right in range(len(s)):
            mp[s[right]]+=1
            while mp[s[right]]>2:
                mp[s[left]]-=1
                if mp[s[left]]==0:
                    del mp[s[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans