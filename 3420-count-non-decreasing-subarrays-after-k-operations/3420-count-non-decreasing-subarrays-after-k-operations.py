class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nxt=[n] * n
        st=[]
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                nxt[i] = st[-1]
            st.append(i)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        LOG = n.bit_length()
        up = [[n] * n for _ in range(LOG)]
        cost = [[0] * n for _ in range(LOG)]
        for i in range(n):
            up[0][i] = nxt[i]
            j = nxt[i]
            cost[0][i] = (nums[i] * (j - i)-(pref[j] - pref[i]))
        for p in range(1, LOG):
            for i in range(n):
                mid = up[p - 1][i]
                if mid < n:
                    up[p][i] = up[p - 1][mid]
                    cost[p][i] = (cost[p - 1][i]+ cost[p - 1][mid])
                else:
                    cost[p][i] = cost[p - 1][i]
        def calculateCost(L, R):
            total = 0
            pos = L
            for p in range(LOG - 1, -1, -1):
                nxt_pos = up[p][pos]
                if nxt_pos <= R:
                    total += cost[p][pos]
                    pos = nxt_pos
            total += (nums[pos] * (R - pos + 1)-(pref[R + 1] - pref[pos]))
            return total
        L = 0
        answer = 0
        for R in range(n):
            while L <= R and calculateCost(L, R) > k:
                L += 1
            answer += R - L + 1
        return answer
