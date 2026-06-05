class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n:int)->int:
            if n<0:
                return 0
            s=str(n)
            @lru_cache(None)
            def dfs(pos,tight,state,prev2,prev1):
                if pos==len(s):
                    return (1,0)
                limit=int(s[pos]) if tight else 9
                total=0
                wave=0
                for d in range(limit+1):
                    ntight=tight and (d==limit)
                    if state==0:
                        if d==0:
                            cnt,wav=dfs(pos+1,ntight,0,0,0)
                        else:
                            cnt,wav=dfs(pos+1,ntight,1,0,d)
                        total+=cnt
                        wave+=wav
                    elif state==1:
                        cnt,wav=dfs(pos+1,ntight,2,prev1,d)
                        total+=cnt
                        wave+=wav
                    else:
                        inc=0
                        if (prev1>prev2 and prev1>d) or (prev1<prev2 and prev1<d):
                            inc=1
                        cnt,wav=dfs(pos+1,ntight,2,prev1,d)
                        total+=cnt
                        wave+=wav+inc*cnt
                return (total,wave)
            return dfs(0,True,0,0,0)[1]
        return solve(num2)-solve(num1-1)
