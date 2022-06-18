from typing import List
from typing import Optional

string1 = "anagram"
string2 = "nagaram"


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            for j in range(len(s) - 1):
                if s[j] > s[j + 1]:
                    temp1 = s[j]
                    s[j] = s[j + 1]
                    s[j + 1] = temp1

        for i in range(len(t)):
            for j in range(len(t) - 1):
                if t[j] > t[j + 1]:
                    temp2 = t[j]
                    t[j] = t[j + 1]
                    t[j + 1] = temp2

        for c in s:
            if s[c] != t[c]:
                return False

        return True

        # if len(s) != len(t):
        #     return False

        # smap, tmap = {}, {}

        # for i in range(len(s)):
        #     smap[s[i]] = 1 + smap.get(s[i], 0)
        #     tmap[t[i]] = 1 + tmap.get(t[i], 0)

        # for c in smap:
        #     if smap[c] != tmap[c]:
        #         return False

        # return True


sol = Solution().isAnagram(string1, string2)
print(sol)
