from collections import defaultdict
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        y_groups = defaultdict(list)
        for x, y in points:
            y_groups[y].append(x)

        combo_count = []
        for xs in y_groups.values():
            cnt = len(xs)
            if cnt >= 2:
                combo_count.append(cnt * (cnt - 1) // 2)

        total_sum = sum(combo_count) % MOD
        total_sum_sq = sum(c * c for c in combo_count) % MOD

        total = (total_sum * total_sum - total_sum_sq) * pow(2, MOD-2, MOD) % MOD
        return total