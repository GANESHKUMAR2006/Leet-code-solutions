class Solution {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);
        int value=1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==value){
                value+=1;
            }
        }
        return value;
    }
}