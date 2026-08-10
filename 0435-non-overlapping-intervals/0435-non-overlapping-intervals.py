class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        end=intervals[0][-1]
        for interval in intervals[1:]:
            start=interval[0]
            if end>start:
                count+=1
                end=min(end,interval[-1])
            else:
                end=interval[-1]
        return count