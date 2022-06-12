from typing import List

# this allows python3 to read type hints provided by leetcode

nums1 = [2, 7, 11, 15]
target1 = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the output type is not necessary, it's only there to give hints
        # self is only needed when you're indicating "method" (function) of a class
        prevMap = {}  # val : index
        # this is a hash map that is currently empty

        for i, n in enumerate(nums):
            # i is the index, n is the value in nums
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
                # prevMap[diff] gives us the index number in nums
            prevMap[n] = i
            # this is a bit counter-intuitive but we actually want to keep
            # track of the order in nums not the value itself
        return


sol = Solution().twoSum(nums1, target1)
print(sol)
