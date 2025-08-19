from typing import List

# Brute force approach
class SolutionBrute:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = set()  # use set to avoid duplicates

        # Check every combination of 4 elements
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quad = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                            res.add(quad)

        return [list(quad) for quad in res]

# Time Complexity: O(n^4)   (4 nested loops)
# Space Complexity: O(m) where m = number of unique quadruplets


# Optimized approach using Sorting + Two Pointers
class SolutionOptimal:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates for i

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # skip duplicates for j

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # skip duplicates for left
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # skip duplicates for right
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res

# Time Complexity: O(n^3)   (two nested loops + two-pointer scan)
# Space Complexity: O(1)    (ignoring sorting cost)
