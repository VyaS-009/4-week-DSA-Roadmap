from typing import List

# Brute force approach
class SolutionBrute:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        l, r = 0, n - 1

        # find first mismatch from the left
        while l < n and nums[l] == sorted_nums[l]:
            l += 1

        # find first mismatch from the right
        while r > l and nums[r] == sorted_nums[r]:
            r -= 1

        return 0 if l == n else r - l + 1

# Time Complexity: O(n log n)   (sorting dominates)
# Space Complexity: O(n)        (extra space for sorted copy)


# Optimized approach using scanning from both sides
class SolutionOptimal:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = -1, -2   # default if already sorted
        max_num, min_num = nums[0], nums[-1]

        # left → right pass: find right boundary
        for i in range(1, n):
            max_num = max(max_num, nums[i])
            if nums[i] < max_num:
                r = i

        # right → left pass: find left boundary
        for i in range(n - 2, -1, -1):
            min_num = min(min_num, nums[i])
            if nums[i] > min_num:
                l = i

        return r - l + 1

# Time Complexity: O(n)     (single pass from both ends)
# Space Complexity: O(1)    (constant extra space)
