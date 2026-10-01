class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for i, num in enumerate(nums):
            if not num - 1 in nums:
                count = 0
                while num + count in nums:
                    count += 1
            
                if count > longest:
                    longest = count
            
        return longest



                
            


            