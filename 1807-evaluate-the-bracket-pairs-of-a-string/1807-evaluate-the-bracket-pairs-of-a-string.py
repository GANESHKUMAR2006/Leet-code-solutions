class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp={}
        for key,value in knowledge:
            mp[key]=value
        idx=0
        n=len(s)
        ans=''
        while idx<n:
            ch=s[idx]
            cur=''
            if ch=='(':
                idx+=1 
                ch=s[idx]
                while ch!=')':
                    cur+=ch
                    idx+=1
                    ch=s[idx]
                if cur not in mp:
                    ans+='?'
                else:
                    ans+=mp[cur]
                idx+=1 
            else:
                ans+=ch
                idx+=1
        return ans