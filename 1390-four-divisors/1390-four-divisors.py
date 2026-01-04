class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def iteration(n):
            hashset=set()
            i=1
            while i*i<=n:
                if n%i==0:
                    hashset.add(i)
                    hashset.add(n//i)
                    if len(hashset)>4:
                        return 0
                i+=1
            return sum(hashset) if len(hashset)==4 else 0
        ans=0
        for val in nums:
            ans+=iteration(val)
        return ans