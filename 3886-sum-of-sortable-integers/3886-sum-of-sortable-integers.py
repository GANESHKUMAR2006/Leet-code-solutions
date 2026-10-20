class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        for k in range(1,n + 1):
            if n%k!=0:
                continue
            valid=True
            for i in range(0,n,k):
                arr=nums[i:i+k]
                m=len(arr)
                descents=0
                for j in range(m):
                    if arr[j]>arr[(j+1)%m]:
                        descents+=1
                if descents>1:
                    valid=False
                    break
                if i>0:
                    prev=nums[i - 1]
            if valid:
                blocks=[]
                for i in range(0,n,k):
                    arr=nums[i:i+k]
                    pivot=next((j for j in range(len(arr) - 1) if arr[j] > arr[j + 1]),-1)
                    if pivot==-1:
                        blocks.append(arr)
                    else:
                        blocks.append(arr[pivot+1:] + arr[:pivot+1])
                for i in range(1,len(blocks)):
                    if blocks[i-1][-1]>blocks[i][0]:
                        valid=False
                        break
            if valid:
                ans+=k
        return ans