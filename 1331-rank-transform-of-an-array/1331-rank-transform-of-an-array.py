class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=sorted(set(arr))
        value={}
        for i,j in enumerate(temp):
            value[j]=i+1
        return [value[x] for x in arr]

