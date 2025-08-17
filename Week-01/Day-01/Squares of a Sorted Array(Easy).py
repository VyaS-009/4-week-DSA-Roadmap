from typing import List

#Brute force approach
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [x*x for x in nums] 
        res.sort()                  
        return res
    
#Time Complexity: O(nlogn)
#Space Complexity: O(n)

#Optimmized approach using two pointers
class Solution:

    def sortedSquares(self, nums:List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        j,k= 0,n-1

        for i in range(k, -1,-1):
            if abs(nums[j]) > abs(nums[k]):
                result[i] = nums[j] ** 2
                j+=1
            else:
                result[i] = nums[k] ** 2
                k-=1
        return result
    
#Time Complexity: O(n)
#Space Complexity: O(n)

        