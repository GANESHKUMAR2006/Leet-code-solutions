class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        ans=[]
        for l in range(len(str(low)),len(str(high))+1):
            for start in range(10-l):
                num=int(s[start:start+l])
                if low<=num<=high:
                    ans.append(num)
        return ans