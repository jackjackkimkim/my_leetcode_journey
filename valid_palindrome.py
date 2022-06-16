from typing import List

string1 = "A man, a plan, a canal: Panama"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newstring = ""

        # for c in s:
        #     if c.isalnum():
        #         newstring += c.lower()
        # return newstring == newstring[::-1]

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True


sol = Solution().isPalindrome(string1)
print(sol)
