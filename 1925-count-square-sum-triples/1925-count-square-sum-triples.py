class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n):
            for j in range(1,n):
                c2=i*i+j*j
                c=int(c2**(0.5))
                if c2==c*c and c<=n: 
                    count+=1
        return count