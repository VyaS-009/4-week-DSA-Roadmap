from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Brute force approach
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        # Collect unique values using a set (or list since it’s sorted)
        values = []
        current = head
        while current:
            if not values or values[-1] != current.val:
                values.append(current.val)
            current = current.next
        
        # Rebuild linked list from unique values
        dummy = ListNode(0)
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next

# Time Complexity: O(n)  (two passes - one to collect, one to rebuild)
# Space Complexity: O(n) (extra list to store values)


# Optimized approach
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# Time Complexity: O(n)  (single pass)
# Space Complexity: O(1) (in-place, no extra data structure)
