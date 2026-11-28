class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        count = [0] * (n + 1)
        min_price = float('inf')
        for f, p in items:
            count[f] += 1
            min_price = min(min_price, p)
        gain = [0] * (n + 1)
        for f in range(1, n + 1):
            total = 0
            for j in range(f, n + 1, f):
                total += count[j]
            gain[f] = total - 1
        deals = []
        for f, p in items:
            if p < 2 * min_price and gain[f] > 0:
                deals.append((p, gain[f]))
        deals.sort()
        ans = 0
        for price, copies in deals:
            take = min(copies, budget // price)
            ans += take * 2
            budget -= take * price
        ans += budget // min_price
        return ans