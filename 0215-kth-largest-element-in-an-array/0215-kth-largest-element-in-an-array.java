import java.util.*;
class Solution {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        k=nums.length-k;
        return nums[k];
    }
}