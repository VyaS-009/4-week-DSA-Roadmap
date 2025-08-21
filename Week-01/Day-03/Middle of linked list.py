from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Brute Force Approach: Count length, then traverse again to middle
class SolutionBrute:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        
        # First pass: count length
        while curr:
            length += 1
            curr = curr.next
        
        # Second pass: move to middle
        mid = length // 2
        curr = head
        for _ in range(mid):
            curr = curr.next
        
        return curr

# Time Complexity: O(n) (two passes)  
# Space Complexity: O(1)  


# Optimized Approach: Fast and Slow Pointers (Tortoise & Hare)
class SolutionOptimal:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        # Move fast by 2 and slow by 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

# Time Complexity: O(n) (single pass)  
# Space Complexity: O(1)  
