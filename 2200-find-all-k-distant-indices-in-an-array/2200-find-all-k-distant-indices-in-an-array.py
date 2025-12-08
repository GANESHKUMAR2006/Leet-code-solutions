class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        pos=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==key:
                pos.append(i)
        left=0
        idx=0
        ans=[]
        while idx<n:
            if pos and left<len(pos):
                if abs(idx-pos[left])<=k:
                        ans.append(idx)
                elif idx>pos[left]:
                    left+=1
                    idx-=1 
            idx+=1
        return ans
