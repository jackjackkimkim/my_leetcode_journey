from typing import List
from typing import Optional

nums1 = [-1, 0, 3, 5, 9, 12]


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return -1


sol = Solution().search(nums1, 9)
print(sol)
