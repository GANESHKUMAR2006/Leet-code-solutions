class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered=[0]*(51)
        for l,r in ranges:
            covered[l]+=1
            if r+1<=50:
                covered[r+1]-=1
        for i in range(1,51):
            covered[i]+=covered[i-1]
        for i in range(left,right+1):
            if covered[i]==0:
                return False
        return True
