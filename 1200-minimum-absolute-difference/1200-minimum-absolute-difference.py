class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        difference=float('inf')
        for i in range(len(arr)-1):
            difference=min(difference,abs(arr[i]-arr[i+1]))
        newlist=[]
        for i in range(0,len(arr)-1):
            if(abs(arr[i]-arr[i+1])==difference):
                newlist.append([arr[i],arr[i+1]])
        return newlist