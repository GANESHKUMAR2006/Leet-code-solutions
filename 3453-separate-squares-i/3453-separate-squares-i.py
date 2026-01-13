class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total=0
        lo=float('inf')
        hi=float('-inf')
        for x,y,l in squares:
            total+=l*l
            lo=min(lo,y)
            hi=max(hi,y+l)
        half=total/2
        def area(main):
            s=0
            for x,y,l in squares:
                if main<=y:
                    continue
                h=min(main-y,l)
                s+=h*l
            return s
        for _ in range(60):
            mid=(lo+hi)/2
            if area(mid)<half:
                lo=mid
            else:
                hi=mid
        return lo