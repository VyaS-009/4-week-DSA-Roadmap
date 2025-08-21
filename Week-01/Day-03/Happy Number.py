from typing import Set

# Brute force approach using HashSet to detect cycles
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen: Set[int] = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

# Time Complexity: O(log n * k)  
#   - log n to compute sum of squares of digits  
#   - k is number of iterations before reaching 1 or repeating  
# Space Complexity: O(k) for the hash set (worst-case storing cycle numbers)


# Optimized approach using Floyd’s Cycle Detection (Tortoise & Hare)
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow, fast = n, get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1

# Time Complexity: O(log n * k)  
#   - Same reasoning as brute, but fewer stored values  
# Space Complexity: O(1) (constant, no extra set)
