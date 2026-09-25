import copy
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = copy.deepcopy(nums)
        for num in nums:
            new_arr.append(num)

        return new_arr

        
            