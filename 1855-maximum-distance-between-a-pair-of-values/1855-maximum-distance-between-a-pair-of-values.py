class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        distance=0
        i=0
        j=0
        n=len(nums1)
        m=len(nums2)
        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                distance=max(distance,j-i)
                j+=1
            else:
                i+=1
                j=max(j,i)
        return distance