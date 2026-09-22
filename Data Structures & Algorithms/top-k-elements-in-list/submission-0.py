class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        num_list = []

        for num in nums:
            num_dict[num] += 1

        count = 0
        while count < k:
            most_frequent = max(num_dict, key=num_dict.get)
            num_list.append(most_frequent)
            del num_dict[most_frequent]
            count += 1


        return num_list