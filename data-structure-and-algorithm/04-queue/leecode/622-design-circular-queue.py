class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.body = [None]*self.size
        self.front = self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.body[self.rear] = value
        self.rear += 1

        if self.rear == self.size:
            self.rear = 0

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.body[self.front] = None
        self.front += 1

        if self.front == self.size:
            self.front = 0

        return True

    def Front(self) -> int:
        return -1 if self.body[self.front] is None else self.body[self.front]

    def Rear(self) -> int:
        return -1 if self.body[self.rear-1] is None else self.body[self.rear-1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.body[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.body[self.front] is not None
