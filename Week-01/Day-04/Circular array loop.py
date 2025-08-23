from typing import List

# Brute Force Approach: Use visited sets to detect cycles
class SolutionBrute:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            visited = set()
            direction = nums[i] > 0  # True = forward, False = backward
            j = i

            while True:
                if (nums[j] > 0) != direction:
                    break  # direction mismatch
                if j in visited:
                    return True if len(visited) > 1 else False
                visited.add(j)
                j = next_index(j)

        return False

# Time Complexity: O(n^2) (for each index, we may traverse up to n elements)
# Space Complexity: O(n) (extra set for visited elements in each attempt)


# Optimized Approach: Floyd’s Cycle Detection + In-place marking
class SolutionOptimal:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i
            direction = nums[i] > 0

            while True:
                # Move slow pointer 1 step
                next_slow = next_index(slow)
                # Move fast pointer 2 steps
                next_fast = next_index(fast)
                if (nums[next_fast] > 0) != direction or nums[fast] == 0:
                    break
                next_fast = next_index(next_fast)
                if (nums[next_fast] > 0) != direction or nums[next_fast] == 0:
                    break

                slow, fast = next_slow, next_fast

                if slow == fast:
                    if slow == next_index(slow):  # cycle of length 1
                        break
                    return True

            # Mark all nodes in this path as 0 (visited) to avoid re-processing
            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                nxt = next_index(j)
                nums[j] = 0
                j = nxt

        return False

# Time Complexity: O(n) (each node is visited at most once)
# Space Complexity: O(1) (no extra space, in-place marking)
