def palindrome(x):
    return str(x)==str(x)[::-1]
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        count=0
        for i in range(1,10000):
            s=str(i)
            x=s+s[:-1][::-1]
            y=int(x)*int(x)
            if y>=int(left) and y<=int(right) and palindrome(y):
                count+=1
            x=s+s[::-1]
            y=int(x)*int(x)
            if y>=int(left) and y<=int(right) and palindrome(y):
                count+=1
        return count