class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
      n=len(s)
      new=['0']*n
      count1=s.count('1')
      new[n-1]='1'
      count1-=1
      for i in range(count1):
        new[i]='1'
      return ''.join(new)