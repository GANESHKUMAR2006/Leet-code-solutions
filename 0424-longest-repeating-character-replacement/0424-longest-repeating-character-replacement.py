class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        mp=defaultdict(int)
        mxfreq=0
        left=0
        ans=0
        for right in range(len(s)):
            mp[ord(s[right])-ord('a')]+=1
            mxfreq=max(mxfreq,mp[ord(s[right])-ord('a')])
            while (right-left+1)-mxfreq>k:
                mp[ord(s[left])-ord('a')]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
