class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        temp=[0]*(n+1)
        prefix=0
        tp=len(temp)
        for i in range(1,tp):
            prefix+=gain[i-1]
            temp[i]=prefix
        return max(temp)