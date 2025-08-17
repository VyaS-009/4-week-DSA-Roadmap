from typing import List

#Brute force approach

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest_sum = float("inf")

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    total = nums[i] + nums[j] + nums[k]
                    if abs(total - target) < abs(closest_sum - target):
                        closest_sum = total
        return closest_sum


#Optiimized approach using two pointers
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result =[]
        n= len(nums)
        nums.sort()
        closest=float('inf')

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            j,k = i+1, n-1

            while j<k:
                total= nums[i]+nums[j]+nums[k]

                if abs(total-target) < abs(closest-target):
                    closest=total
                
                if total==target:
                    return total
                elif total>target:
                    k-=1
                else:
                    j+=1
        return closest
