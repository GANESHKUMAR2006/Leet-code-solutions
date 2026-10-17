class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        digit=[]
        for i,val in enumerate(nums):
            sum_1=0
            while val>0:
                sum_1=sum_1+(val%10)
                val//=10
            digit.append(sum_1)
        target=sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        visited=[False]*n
        swap=0
        pos = {val: i for i, val in enumerate(target)}
        for i in range(n):
            if visited[i]:
                continue
            j = i
            cycle_len = 0
            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_len += 1
            if cycle_len > 1:
                swap += cycle_len - 1
        return swap

                