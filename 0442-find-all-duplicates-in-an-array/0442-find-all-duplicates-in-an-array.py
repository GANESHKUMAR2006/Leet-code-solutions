class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        arr.sort()
        ans=[]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                ans.append(arr[i])
        return ans