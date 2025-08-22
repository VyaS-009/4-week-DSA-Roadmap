from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Brute Force Approach: Use an array to reorder
class SolutionBrute:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # 1. Copy nodes into an array
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next

        # 2. Reorder using two pointers
        i, j = 0, len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            i += 1
            if i == j:
                break
            arr[j].next = arr[i]
            j -= 1

        arr[i].next = None  # terminate list

# Time Complexity: O(n)  
# Space Complexity: O(n) (array storage)


# Optimized Approach: Find middle + reverse second half + merge
class SolutionOptimal:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # cut first half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev  # head of reversed second half

        # 3. Merge two halves
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

# Time Complexity: O(n) (find middle + reverse + merge)  
# Space Complexity: O(1) (in-place manipulation)  
