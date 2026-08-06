class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h=Counter(s)
        ans=''
        for crt in order:
            ans+=crt*h[crt]
        for ch in sorted(s):
            if ch not in ans:
                ans+=ch*h[ch]
        return ans