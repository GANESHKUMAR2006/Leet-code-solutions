class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n=str(n)
        return str(x) in n and n[0]!=str(x)