from typing import List
from typing import Optional


nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        sum = 0

        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            maxSub = max(maxSub, sum)

        return maxSub


sol = Solution().maxSubArray(nums1)
print(sol)
