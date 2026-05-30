from bisect import bisect_left, bisect_right, insort
from typing import List


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAXX = 50000
        n = MAXX + 2

        # iterative segment tree
        seg = [0] * (2 * n)

        def update(pos, val):
            pos += n
            seg[pos] = val
            pos //= 2

            while pos:
                seg[pos] = max(seg[pos * 2], seg[pos * 2 + 1])
                pos //= 2

        def range_max(l, r):
            """max in [l, r]"""
            l += n
            r += n
            res = 0

            while l <= r:
                if l & 1:
                    res = max(res, seg[l])
                    l += 1
                if not (r & 1):
                    res = max(res, seg[r])
                    r -= 1
                l //= 2
                r //= 2

            return res

        # keep obstacles sorted
        obstacles = [0, MAXX + 1]

        # initially one big gap
        update(MAXX + 1, MAXX + 1)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                idx = bisect_left(obstacles, x)

                left = obstacles[idx - 1]
                right = obstacles[idx]

                # split interval
                update(x, x - left)
                update(right, right - x)

                insort(obstacles, x)

            else:
                _, x, sz = q

                idx = bisect_right(obstacles, x)
                prev_obs = obstacles[idx - 1]

                # max completed gap ending <= x
                best_gap = range_max(0, x)

                # unfinished final segment [prev_obs, x]
                best_gap = max(best_gap, x - prev_obs)

                ans.append(best_gap >= sz)

        return ans