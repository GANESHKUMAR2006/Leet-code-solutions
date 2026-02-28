class Solution:
    def concatenatedBinary(self, n: int) -> int:
      string=""
      for i in range(1,n+1):
        ans=format(i,'b')
        string+=ans
      return int(string,2)%(10**9+7)