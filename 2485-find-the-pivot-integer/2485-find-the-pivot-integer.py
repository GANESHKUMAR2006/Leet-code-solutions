class Solution:
    def pivotInteger(self, n: int) -> int:
       pivot=(n*(n+1))//2
       sqrt=int(pivot**(0.5))
       if sqrt**2==pivot:
        return int((pivot)**(0.5))
       else:
        return -1