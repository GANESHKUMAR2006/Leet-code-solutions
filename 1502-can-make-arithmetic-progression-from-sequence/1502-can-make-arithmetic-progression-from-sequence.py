class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        difference=abs(arr[0]-arr[1])
        for i in range(0,len(arr)-1):
            if(abs(arr[i]-arr[i+1])==difference):
                continue;
            elif(abs(arr[i]-arr[i+1])!=difference):
                return False
                break;
        return True