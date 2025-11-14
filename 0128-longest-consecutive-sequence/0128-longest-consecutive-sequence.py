class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         if not nums:
            return 0
         nums.sort()
         cnt=1
         ans=0
         mp=[]
         n=len(nums)
         mp.append(nums[0])
         for i in range(1,n):
            if nums[i-1]!=nums[i]:
                mp.append(nums[i])
         for i in range(1,len(mp)):
            if mp[i-1]+1==mp[i]:
                cnt+=1
            else:
                cnt=1
            ans=max(ans,cnt)
         ans=max(ans,cnt)
         return ans         