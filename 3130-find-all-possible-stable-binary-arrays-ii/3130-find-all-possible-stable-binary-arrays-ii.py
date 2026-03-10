class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        for i in range(1, min(limit, zero) + 1):
            dp0[i][0] = 1
        for j in range(1, min(limit, one) + 1):
            dp1[0][j] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                if i > 0:
                    dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % mod
                    if i - limit - 1 >= 0:
                        dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + mod) % mod
                if j > 0:
                    dp1[i][j] = (dp1[i][j - 1] + dp0[i][j - 1]) % mod
                    if j - limit - 1 >= 0:
                        dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + mod) % mod
        return (dp0[zero][one] + dp1[zero][one]) % mod
