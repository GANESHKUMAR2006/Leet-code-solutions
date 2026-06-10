from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        K = lg[n] + 1

        st_max = [[0] * n for _ in range(K)]
        st_min = [[0] * n for _ in range(K)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        for p in range(1, K):
            half = 1 << (p - 1)
            length = 1 << p

            for i in range(n - length + 1):
                st_max[p][i] = max(
                    st_max[p - 1][i],
                    st_max[p - 1][i + half]
                )
                st_min[p][i] = min(
                    st_min[p - 1][i],
                    st_min[p - 1][i + half]
                )

        def get_value(l, r):
            length = r - l + 1
            p = lg[length]

            mx = max(
                st_max[p][l],
                st_max[p][r - (1 << p) + 1]
            )

            mn = min(
                st_min[p][l],
                st_min[p][r - (1 << p) + 1]
            )

            return mx - mn

        heap = []

        for l in range(n):
            v = get_value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            v, l, r = heapq.heappop(heap)
            ans += -v

            if r > l:
                nr = r - 1
                heapq.heappush(
                    heap,
                    (-get_value(l, nr), l, nr)
                )

        return ans