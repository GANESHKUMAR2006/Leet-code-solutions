class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count=0
        newlist=[]
        for i in range(0,len(nums)):
            if nums[i]==1:
                newlist.append(count)
                count=0
            else:
                count+=1
        for j in range(1,len(newlist)):
            if newlist[j]>=k:
                continue
            else:
                return False
                break
        return True