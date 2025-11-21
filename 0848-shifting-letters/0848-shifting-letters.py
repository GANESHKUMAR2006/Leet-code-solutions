class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
       s=list(s)
       tot=0
       n=len(s)
       for i in range(n-1,-1,-1):
         tot+=shifts[i]
         s[i]=chr(((ord(s[i])-ord('a')+tot)%26)+ord('a'))
       return ''.join(s)