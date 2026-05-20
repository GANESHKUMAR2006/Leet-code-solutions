class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        n=len(a)
        freq=[0]*(n+1)
        common=0
        ans=[]
        for i in range(n):
            freq[a[i]]+=1
            if freq[a[i]]==2:
                common+=1
            freq[b[i]]+=1
            if freq[b[i]]==2:
                common+=1
            ans.append(common)
        return ans