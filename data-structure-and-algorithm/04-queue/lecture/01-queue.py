class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.front = None

    def enqueue(self, val) -> None:
        if not self.front:
            self.front = Node(val)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(val)

    def dequeue(self) -> any:
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.val

    def is_empty(self) -> bool:
        return self.front is None
