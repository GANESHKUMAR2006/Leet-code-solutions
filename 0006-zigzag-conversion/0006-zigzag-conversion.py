class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        ans=['']*numRows
        curr=0
        step=1
        for ch in s:
            ans[curr]+=ch
            if curr==0:
                step=1
            elif curr==numRows-1:
                step=-1
            curr+=step
        return ''.join(ans)