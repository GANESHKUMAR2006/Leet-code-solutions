class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        e=[]
        for x,y,l in squares:
            e.append((y,1,x,x+l))
            e.append((y+l,-1,x,x+l))
        e.sort()
        xs=[]
        prev=e[0][0]
        t=0
        a=[]
        def union(intervals):
            intervals.sort()
            res=cur=0
            end=-10**30
            for a,b in intervals:
                if a>end:
                    res+=b-a
                    end=b
                elif b>end:
                    res+=b-end
                    end=b
            return res
        for y,typ,x1,x2 in e:
            if y>prev and xs:
                h=y-prev
                w=union(xs)
                a.append((prev,h,w))
                t+=h*w
            if typ==1:
                xs.append((x1,x2))
            else:
                xs.remove((x1,x2))
            prev=y
        half=t/2
        acc=0
        for y,h,w in a:
            if acc+h*w>=half:
                return y+(half-acc)/w
            acc+=h*w
        return 0