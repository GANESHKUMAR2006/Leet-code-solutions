class Solution:
    def reverseParentheses(self, s: str) -> str:
        s=list(s)
        n=len(s)
        ans=''
        pair=[]
        st=[]
        for i,ch in enumerate(s):
            if ch=='(':
                st.append(i)
                s[i]='*'
                
            elif ch==')':
                pair.append((st[-1],i))
                s[i]='*'
                st.pop()
        if not pair:
            return ''.join(s)
        def reverse(l,r):
            L=l 
            R=r  
            while L<R:
                s[L],s[R]=s[R],s[L]
                L+=1
                R-=1
        for l,r in pair:
            reverse(l+1,r-1)
        ans=''
        for ch in s:
            if ch!='*':
                ans+=ch
        return ans