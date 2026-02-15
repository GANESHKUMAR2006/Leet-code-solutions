class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec1=0
        dec=0
        for i in a:
            dec=dec*2+int(i)
        for j in b:
            dec1=dec1*2+int(j)
        v=format((dec+dec1),'b')
        return v
        