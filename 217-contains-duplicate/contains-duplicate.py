class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seenNums = set()
        
        for num in nums:
            if num in seenNums:
                return True
            else:
                seenNums.add(num)
        return False