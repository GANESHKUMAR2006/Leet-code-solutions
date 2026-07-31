class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        count=Counter(s)
        order=[]
        for ch,i in count.items():
            order.append((-i,ch))
        order.sort()
        ans=""
        for i,ch in order:
            ans+=ch*(-i)
        return ans
        