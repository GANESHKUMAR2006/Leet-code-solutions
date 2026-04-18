class Solution:
    def mirrorDistance(self, n: int) -> int:
        n=str(n)
        rev=n[::-1]
        return abs(int(rev)-int(n))