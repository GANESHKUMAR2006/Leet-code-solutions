class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        while True:
            if(len(nums)==left):
                return -1
                break;
            if(nums[left]==target):
                return left
                break
            if(nums[left]!=target):
                left=left+1