class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        binary=[]
        for i in range(left,right+1):
            j=format(i,'b')
            binary.append(j.count("1"))
        value=0
        for i in binary:
            count=0
            for j in range(2,i):
                if i%j==0:
                    count=1
                    break
            if (count==0) and (i!=0 and i!=1):
                value+=1
        return value