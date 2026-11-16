class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            temp = 0
            Length = 0
            ans = ''
            for num in s:
                if Length==k:
                    ans+=str(temp)
                    temp = 0
                    Length = 0
                temp+=int(num)
                Length+=1
            if temp or Length:
                ans += str(temp)
            s = str(ans) 

        return s