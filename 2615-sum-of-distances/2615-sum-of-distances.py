class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ord=defaultdict(list)
        for i in range(len(nums)):
            ord[nums[i]].append(i)
        ans=[0]*len(nums)
        for idx in ord.values():
            n=len(idx)
            prefix=[0]*(n+1)
            for i in range(n):
                prefix[i+1]=prefix[i]+idx[i]
            for i in range(n):
                ind=idx[i]
                left=ind*i-prefix[i]
                right=(prefix[n]-prefix[i+1])-ind*(n-i-1)
                ans[ind]=left+right
        return ans