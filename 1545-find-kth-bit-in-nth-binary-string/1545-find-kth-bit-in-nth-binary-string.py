class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s='0'
        for _ in range(2,n+1):
            new=''
            for i in s:
                if i=='0':
                    new+='1'
                else:
                    new+='0'
            new=new[::-1]
            s=s+'1'+new
        return s[k-1]