class Solution:
    def isValid(self, s: str) -> bool:
        brac_dict = {"(": ")","{": "}","[": "]"}
        par_list = []
        for char in s:
            if char in "({[":
                par_list.append(char)
            elif char in ")}]":
                if not par_list:
                    return False
                if brac_dict[par_list[-1]] != char:
                    return False
                par_list.pop()

        if not par_list:
            return True

        return False
            



            
