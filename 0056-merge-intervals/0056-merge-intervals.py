class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        res.append(intervals[0])
        n=len(intervals)
        for i in range(1,n):
            last=res[-1]
            cur=intervals[i]
            if last[1]>=cur[0]:
                last[1]=max(last[1],cur[1])
            else:
                res.append(intervals[i])
        return res