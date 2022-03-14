from tkinter import E
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input = [1, 2, 3, 4]

        # (init)
        node = current = ListNode()     # (step #1)
        node.next = head                # (step #2)

        # (loop)
        while current.next and current.next.next:
            odd = current.next          # (step #1)
            even = current.next.next    # (step #2)
            odd.next = even.next        # (step #3)
            current.next = even         # (step #4)
            current.next.next = odd     # (step #5)
            current = current.next.next  # (step #6)

        # output = [2, 1, 4, 3]
        return node.next


# 테스트 코드
if __name__ == "__main__":
    def add(node, value):
        while node.next:
            node = node.next
        node.next = ListNode(value)

    def pprint(node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        print(values)

    # 연결 리스트 생성
    L1 = ListNode(1)
    for v in [2, 3, 4]:
        add(L1, v)

    solution = Solution()
    pprint(solution.swapPairs(L1))
