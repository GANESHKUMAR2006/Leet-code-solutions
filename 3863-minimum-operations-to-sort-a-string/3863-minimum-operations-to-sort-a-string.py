class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        target = ''.join(sorted(s))
        if s == target:
            return 0
        if n == 2:
            return -1
        left = 0
        while s[left] == target[left]:
            left += 1
        right = n - 1
        while s[right]==target[right]:
            right-=1
        if left>0 or right<n-1:
            return 1
        mn = min(s)
        mx = max(s)
        if s[0] == mx and s[-1] == mn:
            if s.count(mn) == 1 and s.count(mx) == 1:
                return 3
        return 2