# <문제>
"""
연결 리스트를 정렬하라
"""

# <입력>
"""
1) Line 1 : ListNode([])
"""




from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        arr.sort(reverse=True)

        head = node = ListNode()

        for _ in range(len(arr)):
            num = arr.pop()
            node.next = ListNode(num)
            node = node.next

        return head.next


if __name__ == "__main__":
    cases = [
        [4, 2, 1, 3],
        [-1, 5, 3, 4, 0]
    ]
    outputs = [
        [1, 2, 3, 4],
        [-1, 0, 3, 4, 5]
    ]

    solution = Solution()

    for case, output in zip(cases, outputs):
        head = node = ListNode()
        for val in case:
            node.next = ListNode(val)
            node = node.next
        head = head.next

        linkedList = solution.sortList(head)
        arr = []

        while linkedList:
            arr.append(linkedList.val)
            linkedList = linkedList.next
        print(arr == output)
