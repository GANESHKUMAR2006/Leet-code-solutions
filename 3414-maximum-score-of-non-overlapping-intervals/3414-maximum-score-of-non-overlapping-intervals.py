from typing import List
from bisect import bisect_left


class Solution:

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        n = len(intervals)

        arr = []

        for i, (l, r, w) in enumerate(intervals):
            arr.append((r, l, w, i))

        arr.sort()

        rights = [x[0] for x in arr]

        prev = [0] * n

        for i in range(n):
            l = arr[i][1]

            # Number of intervals whose right < current left
            prev[i] = bisect_left(rights, l, 0, i)

        # dp[i][k] = (maximum score, lexicographically smallest indices)
        dp = [
            [(0, ()) for _ in range(5)]
            for _ in range(n + 1)
        ]

        for i in range(1, n + 1):

            r, l, w, org = arr[i - 1]

            for k in range(5):

                # Don't take current interval
                best = dp[i - 1][k]

                # Take current interval
                if k > 0:

                    oldscore, oldidx = dp[prev[i - 1]][k - 1]

                    candidatescore = oldscore + w

                    candidateidx = tuple(
                        sorted(oldidx + (org,))
                    )

                    if candidatescore > best[0]:
                        best = (candidatescore, candidateidx)

                    elif (
                        candidatescore == best[0]
                        and candidateidx < best[1]
                    ):
                        best = (candidatescore, candidateidx)

                dp[i][k] = best

        return list(dp[n][4][1])