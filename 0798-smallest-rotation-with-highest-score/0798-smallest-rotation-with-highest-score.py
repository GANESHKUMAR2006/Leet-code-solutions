class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n=len(nums)
        change=[0]*n
        for i,x in enumerate(nums):
            left=(i-x+1)%n
            right=(i+1)%n
            change[left]-=1
            change[right]+=1
            if left>right:
                change[0]-=1
        best=-n
        score=0
        ans=0
        for i in range(n):
            score+=change[i]
            if score>best:
                best=score
                ans=i
        return ans