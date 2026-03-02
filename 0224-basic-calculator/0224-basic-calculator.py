class Solution:
    def calculate(self, s: str) -> int:
        st=[]
        result=0
        sign=1
        number=0
        for c in s:
            if c.isdigit():
                number=number*10+int(c)
            elif c=='+':
                result+=sign*number
                number=0
                sign=1
            elif c=='-':
                result+=sign*number
                number=0
                sign=-1
            elif c=='(':
                st.append(result)
                st.append(sign)
                result=0
                sign=1
            elif c==')':
                result+=sign*number
                number=0
                sign=st.pop()
                res=st.pop()
                result=res+result*sign
        result+=sign*number
        return result