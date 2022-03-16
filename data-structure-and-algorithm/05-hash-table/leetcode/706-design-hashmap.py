class Node:
    def __init__(self, key, val, next=None) -> None:
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.size = 100
        self.maps = [None]*self.size

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, val: int) -> None:
        i = self.hash(key)
        node = self.maps[i]

        if node is None:
            self.maps[i] = Node(key, val)
            return

        while node:
            if node.key == key:
                node.val = val
                return
            if node.next is None:
                break
            node = node.next

        node.next = Node(key, val)

    def get(self, key: int) -> int:
        i = self.hash(key)
        node = self.maps[i]

        if node is None:
            return -1

        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        i = self.hash(key)
        node = self.maps[i]

        if node is None:
            return

        if node.key == key:
            self.maps[i] = node.next if node.next else None
            return

        pred = node
        while node:
            if node.key == key:
                pred.next = node.next
                return
            pred = node
            node = node.next
