class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        temp=[0]*(n)
        for i in range(n):
            binary=format(nums[i],'b')
            count=0
            temp_bin=binary
            while temp_bin!=temp_bin[::-1]:
                temp_bin=format(int(temp_bin,2)+1,'b')
                count+=1
            count2=0
            temp_bin2=binary
            while temp_bin2!=temp_bin2[::-1]:
                temp_bin2=format(int(temp_bin2,2)-1,'b')
                count2+=1
            temp[i]=min(count,count2)
        return temp