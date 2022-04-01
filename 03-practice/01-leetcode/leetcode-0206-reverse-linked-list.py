from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, node = head, None

        while current:
            next = current.next
            current.next = node
            node = current
            current = next

        return node


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
    L = ListNode(1)
    for v in [2, 3, 4, 5]:
        add(L, v)

    solution = Solution()
    pprint(solution.reverseList(L))
