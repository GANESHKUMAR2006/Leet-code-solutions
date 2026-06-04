def checkvalue(n):
    val=str(n)
    if len(val)<3:
        return 0
    cnt=0
    length=len(val)
    for i in range(1,length-1):
        if val[i-1]<val[i] and val[i+1]<val[i]:
            cnt+=1
        if val[i-1]>val[i] and val[i+1]>val[i]:
            cnt+=1
    return cnt

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count=0
        for i in range(num1,num2+1):
            if checkvalue(i):
                waviness=checkvalue(i)
                count+=waviness
        return count
            