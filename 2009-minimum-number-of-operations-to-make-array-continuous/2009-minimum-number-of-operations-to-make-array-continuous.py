class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        ans=n
        new=sorted(set(nums))
        for i in range(len(new)):
            left=new[i]
            right=left+n-1
            crt=bisect_right(new,right)
            j=crt-i
            ans=min(ans,n-j)
        return ans