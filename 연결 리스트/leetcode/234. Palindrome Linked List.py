from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        if not head:
            return True

        node = head
        while node:
            arr.append(node.val)
            node = node.next

        while len(arr) > 1:
            if arr.pop(0) != arr.pop():
                return False

        return True


l1 = LinkedList()

for val in [1, 2, 2, 1]:
    l1.append(val)


solution = Solution()
print(solution.isPalindrome(l1.head))
