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

        '''
        # 첫 번째 실행 과정
            current: ListNode: [1 -> 2 -> 3 -> 4 -> 5]
            
            1) next = ListNode: [2 -> 3 -> 4 -> 5]
            2) current.next = None
            3) node = ListNode: [1]
            4) current = ListNode: [2 -> 3 -> 4 -> 5]
        
        # 두 번째 실행 과정
            current: ListNode: [2 -> 3 -> 4 -> 5]

            1) next = ListNode: [3 -> 4 -> 5]
            2) current.next = ListNode: [1]
            3) node = ListNode: [2 -> 1]
            4) current = ListNode: [3 -> 4 -> 5]

        # 세 번째 실행 과정
            current: ListNode: [3 -> 4 -> 5]

            1) next = ListNode: [4 -> 5]
            2) current.next = ListNode: [2 -> 1]
            3) node = ListNode: [3 -> 2 -> 1]
            4) current = ListNode: [4 -> 5]

        # 네 번째 실행 과정
            current: ListNode: [4 -> 5]
            
            1) next = ListNode: [5]
            2) current.next = ListNode: [3 -> 2 -> 1]
            3) node = ListNode: [4 -> 3 -> 2 -> 1]
            4) current = ListNode: [5]

        # 다섯 번째 실행 과정
            current: ListNode: [5]
            
            1) next = None
            2) current.next = ListNode: [4 -> 3 -> 2 -> 1]
            3) node = ListNode: [5 -> 4 -> 3 -> 2 -> 1]
            4) current = ListNode: None

        # 여섯 번째 실행 과정
            current : None : 반복 종료

        # 최종 반환
            node : ListNode: [5 -> 4 -> 3 -> 2 -> 1]
        '''

        return node
