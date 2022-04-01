class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val)

    def print(self):
        if not self.head:
            return []

        arr = []
        node = self.head
        while node:
            arr.append(node.val)
            node = node.next

        return arr
