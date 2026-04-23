class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap=defaultdict(int)
        for i in nums1:
            for j in nums2:
                hashmap[i+j]+=1
        count=0
        for i in nums3:
            for j in nums4:
                target=-(i+j)
                if target in hashmap:
                    count+=hashmap[target]
        return count