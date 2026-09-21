class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in num_hash:
                return [num_hash[difference],i]
            else:
                num_hash[nums[i]] = i 

 