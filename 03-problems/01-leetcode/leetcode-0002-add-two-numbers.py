from tkinter import E
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values1 = []
        while list1:
            values1.append(list1.val)
            list1 = list1.next
        values1.reverse()
        values1 = int(''.join([str(x) for x in values1]))

        values2 = []
        while list2:
            values2.append(list2.val)
            list2 = list2.next
        values2.reverse()
        values2 = int(''.join([str(x) for x in values2]))

        head = node = ListNode()
        values3 = list(str(values1 + values2))
        while values3:
            value = values3.pop()
            node.next = ListNode(value)
            node = node.next

        return head.next


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
    L1 = ListNode(2)
    for v in [4, 3]:
        add(L1, v)

    L2 = ListNode(5)
    for v in [6, 4]:
        add(L2, v)

    solution = Solution()
    pprint(solution.addTwoNumbers(L1, L2))
