from optparse import Option
from tkinter import E
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head

        return head


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
    for v in [2, 3, 4, 5]:
        add(L1, v)

    solution = Solution()
    pprint(solution.oddEvenList(L1))
