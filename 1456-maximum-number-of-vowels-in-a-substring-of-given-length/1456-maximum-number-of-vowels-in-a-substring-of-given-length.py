class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        left=0
        ans=0
        vowel=set('aeiou')
        for right in range(len(s)):
            if s[right] in vowel:
                count+=1
            while right-left+1>k:
                if s[left] in vowel:
                    count-=1
                left+=1
            if right-left+1==k:
                ans=max(ans,count)
        return ans
        
            