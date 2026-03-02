class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff<0:
            return False
        mp={}
        size=valueDiff+1
        for right in range(len(nums)):
            num=nums[right]
            bucket=num//size
            if bucket in mp:
                return True
            if bucket-1 in mp and abs(num-mp[bucket-1])<=valueDiff:
                return True
            if bucket+1 in mp and abs(num-mp[bucket+1])<=valueDiff:
                return True
            mp[bucket]=num
            if right>=indexDiff:
                old=nums[right-indexDiff]
                old=old//size
                del mp[old]
        return False

            