class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        mylist=[]
        num=0
        length=len(nums)
        for i in range(1,length+1):
            if(length%i==0):
                mylist.append(i)
        for j in mylist:
            num=nums[j-1]*nums[j-1]+num
        return num
        