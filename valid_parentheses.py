from typing import List

string1 = "()[]{}"
string2 = "{[}]"


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_p = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in valid_p:
                if stack and stack[-1] == valid_p[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


sol1 = Solution().isValid(string1)
print(sol1)
sol2 = Solution().isValid(string2)
print(sol2)
