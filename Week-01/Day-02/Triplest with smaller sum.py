from typing import List

# Brute force approach
class Solution:
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] < target:
                        count += 1
        return count

# Time Complexity: O(n^3)   (3 nested loops)
# Space Complexity: O(1)


# Optimized approach using Sorting + Two Pointers
class Solution:
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < target:
                    # All elements between j and k will work, this is optimal rather than using count+=1
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count

# Time Complexity: O(n^2)   (outer loop + two-pointer scan)
# Space Complexity: O(1)    (ignoring sorting cost, done in-place)
