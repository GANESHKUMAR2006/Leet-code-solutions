class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        num=1
        for length in range(1,k+1):
            if num%k==0:
                return length
            num=(num*10+1)%k
        return -1