class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count=Counter(nums)
        ans=sorted([(-j,i) for i,j in count.items()])
        return [j for i,j in ans[:k]]