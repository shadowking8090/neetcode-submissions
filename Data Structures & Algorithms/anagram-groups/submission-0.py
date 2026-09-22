class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        anagram_list = []

        for word in strs:
            if "".join(sorted(word)) in anagram_dict:
                anagram_dict["".join(sorted(word))].append(word)
            else:
                anagram_dict["".join(sorted(word))] = [word]

        for item in anagram_dict.values():
            anagram_list.append(item)

        return anagram_list
