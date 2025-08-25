from typing import List

# Brute Force Approach: Check all subarrays of length k
class SolutionBrute:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = 0

        for i in range(n - k + 1):  # loop through all subarrays of size k
            window = nums[i:i+k]
            if len(set(window)) == k:  # check if all elements are distinct
                max_sum = max(max_sum, sum(window))

        return max_sum

# Time Complexity: O(n * k)  (for each subarray, creating set and summing takes O(k))
# Space Complexity: O(k) (for storing elements in the set)


# Optimized Approach: Sliding Window + HashMap (to check distinct elements quickly)
class SolutionOptimal:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}   # frequency map
        curr_sum = 0
        max_sum = 0

        left = 0
        for right in range(n):
            curr_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1

            # shrink window if size > k
            if right - left + 1 > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                curr_sum -= nums[left]
                left += 1

            # check if current window size == k and all elements are distinct
            if right - left + 1 == k and len(count) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum

# Time Complexity: O(n) (each element enters and leaves the window at most once)
# Space Complexity: O(k) (hashmap for tracking frequencies)
