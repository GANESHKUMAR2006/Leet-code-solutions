class Solution:
    def reverseDegree(self, s: str) -> int:
        newstring="zyxwvutsrqponmlkjihgfedcba"
        counter=0
        for i in range(0,len(s)):
            count=(newstring.find(s[i])+1)*(i+1)
            counter+=count
        return counter
