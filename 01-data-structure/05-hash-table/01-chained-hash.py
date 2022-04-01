import hashlib

# 체인법(오픈 해시)


class Node:
    def __init__(self, key: int or str, val: any, next=None) -> None:
        self.key = key
        self.val = val
        self.next = next


class ChaindHash:
    def __init__(self, size: int) -> None:
        self.size = size
        self.table = [None]*size

    def hashing(self, key: int) -> int:
        if isinstance(key, int):
            return key % self.size

        byte_str = str(key).encode()
        byte_hash = hashlib.sha256(byte_str)
        hash = int(byte_hash.hexdigest(), 16)
        return hash % self.size

    def get(self, key: int) -> any:
        hash = self.hashing(key)
        node = self.table[hash]

        while node is not None:
            if node.key == key:
                return node.val
            node = node.next

        return None

    def set(self, key: int, val: any) -> bool:
        if self.get(key) is not None:
            return False

        hash = self.hashing(key)
        node = Node(key, val, self.table[hash])
        self.table[hash] = node
        return True

    def remove(self, key: int) -> bool:
        hash = self.hashing(key)
        node = self.table[hash]
        pred = None

        while node is not None:
            if node.key == key:
                if pred is None:
                    self.table[hash] = node.next
                else:
                    pred.next = node.next
                return True
            pred = node
            node = node.next
        return False


hash_map = ChaindHash(5)
print(hash_map.set(1, 10))
print(hash_map.set(2, 30))
print(hash_map.get(0))
print(hash_map.get(1))
