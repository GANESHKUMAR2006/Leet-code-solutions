/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    mp=new Map()
    for(i=0;i<nums.length;i++)
    {
        complement=target-nums[i]
        if(mp.has(complement)){
            return [mp.get(complement),i]
        }
        mp.set(nums[i],i)
    }
};