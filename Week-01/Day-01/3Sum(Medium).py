from typing import List
#Brute Force
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()  # use set to avoid duplicates

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        
        return list(result)
#Time Complexity: O(n^3)
#Space Complexity: O(m) where m is the number of unique triplets found


# Optimized approach using two pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1, n-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums [j+1]:
                        j+=1
                    while j < k and nums[k] == nums [k-1]:
                        k-=1
                    j+=1
                    
                elif total > 0:
                    k-=1
                else:
                    j+=1
        return result


#Time Complexity: O(n^2)
#Space Complexity: O(1)

            