class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1]-x[0],reverse=True)
        e=0
        ans=0
        for a,m in tasks:
            if e<m:
                extra=m-e
                ans+=extra
                e+=extra
            e-=a
        return ans