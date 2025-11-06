class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev=str(num)[::-1]
        rev=int(rev)
        rev=str(rev)[::-1]
        return int(rev)==num