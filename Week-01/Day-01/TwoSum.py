from typing import List

# Brute force approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n): #O(n)
            for j in range(i+1, n): #O(n)
                if nums[i] + nums[j] == target:
                    return [i, j]

# Time Complexity: O(n^2)   (nested loops)
# Space Complexity: O(1)


# Optimized approach using HashMap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i, num in enumerate(nums): #O(n)
            if target - num in arr:
                return [i, arr[target - num]]
            arr[num] = i

# Time Complexity: O(n)   (single pass with dictionary lookups)
# Space Complexity: O(n)  (hashmap stores seen numbers)
