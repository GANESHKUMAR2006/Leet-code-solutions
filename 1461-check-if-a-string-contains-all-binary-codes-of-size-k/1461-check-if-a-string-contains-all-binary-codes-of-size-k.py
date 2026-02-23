class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        size=1<<k
        hashset=set()
        n=len(s)
        for i in range(n-k+1):
            hashset.add(s[i:i+k])
            if len(hashset)==size:
                return True
        return False