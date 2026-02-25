class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        ans=0
        left=0
        mp=defaultdict(int)
        for right in range(len(fruits)):
            mp[fruits[right]]+=1
            while len(mp)>2:
                mp[fruits[left]]-=1
                if mp[fruits[left]]==0:
                    del mp[fruits[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans