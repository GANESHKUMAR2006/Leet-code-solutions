class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        st=[]
        for i in range(n):
            data=nums[i]
            left=i
            right=i
            while st and st[-1][0]>nums[i]:
                topval,topleft,topright=st.pop()
                data=max(data,topval)
                left=topleft
            st.append((data,left,right))
        for val,left,right in st:
            for j in range(left,right+1):
                ans[j]=val
        return ans