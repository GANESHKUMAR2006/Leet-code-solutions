class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        count = 0
        while n>=take:
            n-=take
            take-=1
            count+=1
        return count%2==1