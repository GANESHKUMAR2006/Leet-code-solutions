class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>9*num or sum<0:
            return ""
        resdigits=[]
        for _ in range(num):
            digits=min(9,sum)
            resdigits.append(str(digits))
            sum-=digits
        return ''.join(resdigits)