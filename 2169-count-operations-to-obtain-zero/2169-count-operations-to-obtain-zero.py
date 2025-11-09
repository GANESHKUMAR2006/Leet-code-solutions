class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count=0
        if(num1==0 or num2==0):
            return 0
        while num1>0 or num2>0:
            if(num1==num2):
                count+=1
                break;
            var=abs(num1-num2)
            if(num1<num2):
                num2=var
                count+=1
            elif(num2<num1):
                num1=var
                count+=1
        return count
            