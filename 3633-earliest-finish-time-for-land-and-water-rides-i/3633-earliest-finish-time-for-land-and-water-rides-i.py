class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        finishtime=float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                landend=landStartTime[i]+landDuration[i]
                waterstart=max(waterStartTime[j],landend)
                waterend=waterstart+waterDuration[j]
                finishtime=min(finishtime,waterend)
                waterend=waterStartTime[j]+waterDuration[j]
                landstart=max(landStartTime[i],waterend)
                landend=landstart+landDuration[i]
                finishtime=min(finishtime,landend)
        return finishtime