class Solution {
    public boolean search(int[] nums, int target) {
        boolean val=false;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==target){
                val=true;
            }
        }
        return val;
    }
}