from typing import List

# Brute force approach
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                if product < k:
                    count += 1
                else:
                    break  # further elements will only increase the product
        return count

# Time Complexity: O(n^2)   (nested loops, worst-case all subarrays checked)
# Space Complexity: O(1)


# Optimized approach using Sliding Window
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: 
            return 0  # no positive product can be less than 1

        product = 1
        count = 0
        left = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            # all subarrays ending at right and starting from [left...right] are valid
            count += (right - left + 1)

        return count

# Time Complexity: O(n)     (each element visited at most twice by left/right)
# Space Complexity: O(1)
