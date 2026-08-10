class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k==0:
            freq=Counter(nums)
            return sum(1 for x in freq if freq[x]>=2)
        count=0
        seen=set(nums)
        for num in seen:
            if num+k in seen:
                count+=1
        return count