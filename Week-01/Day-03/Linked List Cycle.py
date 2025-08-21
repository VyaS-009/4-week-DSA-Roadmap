# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Brute Force approach using HashSet
class SolutionBrute:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()

        curr = head
        while curr:
            if curr in visited:
                return True  # cycle detected
            visited.add(curr)
            curr = curr.next

        return False

# Time Complexity: O(n)   (traverse all nodes once)
# Space Complexity: O(n)  (store visited nodes in set)


# Optimized approach using Floyd’s Tortoise and Hare Algorithm
class SolutionOptimal:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False  # reached end, no cycle
            slow = slow.next
            fast = fast.next.next

        return True

# Time Complexity: O(n)   (at most 2n steps: slow and fast pointers traverse list)
# Space Complexity: O(1)  (constant extra memory)
