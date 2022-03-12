from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def link(node, value):
    while node.next:
        node = node.next
    node.next = ListNode(value)


def show(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(values)


class Solution:
    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        # (그림 #0)
        head = current = ListNode(0)

        # (그림 #5)까지 반복
        # (그림 #6)부터 종료
        while node1 and node2:

            # (그림 #1 ~ #5)
            if node1.val < node2.val:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next

            current = current.next

        # (그림 #6)
        if node1:
            current.next = node1
        elif node2:
            current.next = node2

        # (그림 #7)
        return head.next


L1 = ListNode(1)
for v in [2, 4]:
    link(L1, v)

L2 = ListNode(1)
for v in [3, 4]:
    link(L2, v)


solution = Solution()
show(solution.mergeTwoLists(L1, L2))
