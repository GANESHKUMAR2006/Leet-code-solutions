class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={0:1}
        count=0
        prefix=0
        for i in nums:
            prefix+=i
            if prefix-k in mp:
                count+=mp[prefix-k]
            mp[prefix]=mp.get(prefix,0)+1
        return count