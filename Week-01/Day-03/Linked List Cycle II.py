# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Brute force approach using HashSet
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr  # first node where cycle begins
            visited.add(curr)
            curr = curr.next

        return None

# Time Complexity: O(n)   (traverse all nodes once)
# Space Complexity: O(n)  (store visited nodes)


# Optimized approach using Floyd’s Cycle Detection (Tortoise & Hare)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow, fast = head, head
        has_cycle = False

        # Step 1: Detect if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None  # no cycle

        # Step 2: Find the cycle start node
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # start of cycle

# Time Complexity: O(n)   (at most 2 passes: detect + find entry)
# Space Complexity: O(1)  (constant extra memory)
