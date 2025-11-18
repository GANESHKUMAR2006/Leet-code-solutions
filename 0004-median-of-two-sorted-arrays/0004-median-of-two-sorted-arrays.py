class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        var=sorted(nums1+nums2)
        n=len(var)//2
        if(len(var)%2==0):
            k=(var[n]+var[n-1])/2
        else:
            k=var[n]
        return float(k)