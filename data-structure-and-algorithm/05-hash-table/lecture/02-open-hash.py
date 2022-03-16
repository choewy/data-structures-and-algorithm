import hashlib
from enum import Enum

# 오픈 주소법(닫힌 해시)


class Status(Enum):
    SAVED = 0
    NULL = 1
    REMOVED = 2


class Bucket:
    def __init__(self, key=None, val=None, status=Status.NULL) -> None:
        self.key, self.val = key, val
        self.status = status

    def set(self, key, val, status) -> None:
        self.key, self.val = key, val
        self.status = status

    def setStatus(self, status) -> None:
        self.status = status


class OpenHash:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [Bucket()]*size

    def hashing(self, key: int) -> int:
        if isinstance(key, int):
            return key % self.size

        byte_str = str(key).encode()
        byte_hash = hashlib.sha256(byte_str)
        hash = int(byte_hash.hexdigest(), 16)
        return hash % self.size

    def rehashing(self, key: int) -> int:
        hash = self.hashing(key) + 1
        return hash % self.size

    def bucket(self, key: int) -> Bucket:
        hash = self.hashing(key)
        bucket = self.table[hash]
        for _ in range(self.size):
            if bucket.status == Status.NULL:
                break
            elif bucket.status == Status.SAVED and bucket.key == key:
                return bucket
            hash = self.rehashing(hash)
            bucket = self.table[hash]
        return None

    def search(self, key: int) -> any:
        bucket = self.bucket(key)
        return None if bucket is None else bucket.val

    def add(self, key: int, val: any) -> bool:
        if self.search(key) is not None:
            return False

        hash = self.hashing(key)
        bucket = self.table[hash]
        for _ in range(self.size):
            if bucket.status == Status.NULL or bucket.status == Status.REMOVED:
                self.table[hash] = Bucket(key, val, Status.SAVED)
                return True

            hash = self.rehashing(hash)
            bucket = self.table[hash]

        return False

    def remove(self, key: int) -> bool:
        bucket = self.bucket(key)
        if bucket is None:
            return False

        bucket.status = Status.REMOVED
        return True


if __name__ == "__main__":
    open_hash = OpenHash(10)
    print(open_hash.add(1, 10))
    print(open_hash.add(2, 30))
    print(open_hash.add(3, 50))
    print(open_hash.search(2))
    print(open_hash.search(4))
