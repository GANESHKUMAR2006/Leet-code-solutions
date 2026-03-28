class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n=len(lcp)
        for i in range(n):
            if lcp[i][i]!=n-i:
                return ""
        word=['']*n
        ch=ord('a')
        for i in range(n):
            if word[i]=='':
                if ch>ord('z'):
                    return ''
                word[i]=chr(ch)
                for j in range(i+1,n):
                    if lcp[i][j]>0:
                        word[j]=chr(ch)
                ch+=1
        dp=[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if word[i]==word[j]:
                    if i==n-1 or j==n-1:
                        dp[i][j]=1
                    else:
                        dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=0
                if dp[i][j]!=lcp[i][j]:
                    return ''
        return ''.join(word)