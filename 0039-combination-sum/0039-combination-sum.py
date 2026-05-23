class Solution:
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        res=[]
        def sm(idx,ans,s):
            if idx==len(c) or s>t:
                return
            if t==s:
                res.append(ans[:])
                return
            ans.append(c[idx])
            sm(idx,ans,s+c[idx])
            ans.pop()
            sm(idx+1,ans,s)
        sm(0,[],0)
        return res