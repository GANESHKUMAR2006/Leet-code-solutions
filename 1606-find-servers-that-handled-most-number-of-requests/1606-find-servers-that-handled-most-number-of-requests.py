class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        bit = [0] * (k + 1)
        def update(i, val):
            i += 1
            while i <= k:
                bit[i] += val
                i += i & -i
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res
        def findKth(target):
            idx = 0
            step = 1 << (k.bit_length() - 1)
            while step:
                nxt = idx + step
                if nxt <= k and bit[nxt] < target:
                    idx = nxt
                    target -= bit[nxt]
                step >>= 1
            return idx
        for i in range(k):
            update(i, 1)
        busy = []
        count = [0] * k
        for i in range(len(arrival)):
            t = arrival[i]
            while busy and busy[0][0] <= t:
                end, server = heapq.heappop(busy)
                update(server, 1)
            total = query(k)
            if total == 0:
                continue
            preferred = i % k
            before = query(preferred)
            if total > before:
                target = before + 1
            else:
                target = 1
            server = findKth(target)
            update(server, -1)
            count[server] += 1
            heapq.heappush(busy,(t + load[i], server))
        maximum = max(count)
        return [i for i in range(k) if count[i] == maximum]