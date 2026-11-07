class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        available = []
        busy = []
        for i in range(n):
            heapq.heappush(available, (servers[i], i))

        ans = []
        curr_time = 0

        for j in range(len(tasks)):
            curr_time = max(curr_time, j)
            while busy and busy[0][0] <= curr_time:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))
            if not available:
                curr_time = busy[0][0]
                while busy and busy[0][0] <= curr_time:
                    free_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))
            weight, idx = heapq.heappop(available)
            ans.append(idx)
            heapq.heappush(
                busy,
                (curr_time + tasks[j], weight, idx)
            )

        return ans
