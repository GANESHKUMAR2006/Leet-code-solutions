class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid={0,1,2,5,8,6,9}
        change={2,5,6,9}
        count=0
        for num in range(1,n+1):
            val=str(num)
            good=False
            for i in val:
                i=int(i)
                if i not in valid:
                    good=False
                    break
                elif i in change:
                    good=True
            if good:
                count+=1
        return count