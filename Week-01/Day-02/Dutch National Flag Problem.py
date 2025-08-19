from typing import List

# Brute force approach (Counting sort style)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = count1 = count2 = 0

        # Count occurrences of 0, 1, 2
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Rewrite the array in-place
        i = 0
        for _ in range(count0):
            nums[i] = 0
            i += 1
        for _ in range(count1):
            nums[i] = 1
            i += 1
        for _ in range(count2):
            nums[i] = 2
            i += 1

# Time Complexity: O(n)   (two passes: count + overwrite)
# Space Complexity: O(1)


# Optimized approach (Dutch National Flag / 3-way partitioning)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        # Process elements with three pointers
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Time Complexity: O(n)   (single scan)
# Space Complexity: O(1)
