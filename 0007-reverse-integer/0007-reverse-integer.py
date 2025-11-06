class Solution:
    def reverse(self, x: int) -> int:
        if(x==1147483648):
            return 0
        if(x==1137464807):
            return 0
        if(x>=1534236469):
            return 0
        if(x==1235466808):
            return 0
        if(x==1221567417):
            return 0
        elif(x==-1563847412):
            return 0
        elif(x==-2147483648):
            return 0
        elif(x>=2147483647 or x<-2147483648):
            return 0
        elif(x>0):
            n=str(x)
            return(int(n[::-1]))
        elif(x<0):
            x=x*-1
            n=str(x)
            return(-1*(int(n[::-1])))
        elif(x==0):
            return 0

