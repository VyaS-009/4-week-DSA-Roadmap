from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Brute Force Approach: Copy values into an array
class SolutionBrute:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr = head
        
        # Copy linked list values into array
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        # Check palindrome property using two pointers
        i, j = 0, len(vals) - 1
        while i < j:
            if vals[i] != vals[j]:
                return False
            i += 1
            j -= 1
        
        return True

# Time Complexity: O(n) (iterate + check)  
# Space Complexity: O(n) (store list values)


# Optimized Approach: Reverse second half in-place
class SolutionOptimal:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1. Find middle (slow ends at mid)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev  # Head of reversed second half

        # 3. Compare first and second half
        first, second = head, second_half
        while second:  # only need to check second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

# Time Complexity: O(n) (find middle + reverse + compare)  
# Space Complexity: O(1) (in-place reversal, no extra array)  
