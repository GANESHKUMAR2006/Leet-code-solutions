class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows={}
        for row,seat in reservedSeats:
            if row not in rows:
                rows[row]=set()
            rows[row].add(seat)
        res=(n-len(rows))*2
        for seats in rows.values():
            left=all(seat not in seats for seat in [2,3,4,5])
            middle=all(seat not in seats for seat in[4,5,6,7])
            right=all(seat not in seats for seat in [6,7,8,9])
            if left and right:
                res+=2
            elif left or middle or right:
                res+=1
        return res