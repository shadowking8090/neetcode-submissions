class Solution:
    def isPalindrome(self, s: str) -> bool:
        f_str = ([char.lower() for char in s if char.isalpha() or (ord(char) <= 57 and ord(char) >= 48)])
        left = 0
        right = len(f_str) - 1

        print(f_str)
        while left < right:
            if f_str[left] != f_str[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
