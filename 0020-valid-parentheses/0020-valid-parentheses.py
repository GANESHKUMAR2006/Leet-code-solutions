class Solution:
    def isValid(self, s: str) -> bool:
        stack=[0]
        if(len(s)==1):
            return False
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i)
            elif(stack[-1]!='{' and i=='}'):
                stack.append(i)
                break;
            elif(stack[-1]!='(' and i==')'):
                stack.append(i)
                break;
            elif(stack[-1]!='[' and i==']'):
                stack.append(i)
                break;
            elif(stack[-1]=='{' and i=='}'):
                stack.pop()
            elif(stack[-1]=='(' and i==')'):
                stack.pop()
            elif(stack[-1]=='[' and i==']'):
                stack.pop()
        return len(stack)==1