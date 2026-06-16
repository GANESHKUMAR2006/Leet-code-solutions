class Solution:
    def processStr(self, s: str) -> str:
        newstring=""
        for i in s:
            if i=="#":
                newstring+=newstring
            elif i=="%":
                newstring=newstring[::-1]
            elif i=="*":
                newstring=newstring[:len(newstring)-1]
            else:
                newstring+=i
        return newstring