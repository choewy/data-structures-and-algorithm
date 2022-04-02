class MyQueue:
    def __init__(self):
        self.body = []

    def push(self, x: int) -> None:
        self.body.append(x)

    def pop(self) -> int:
        val = self.body[0]
        self.body = self.body[1:]
        return val

    def peek(self) -> int:
        return self.body[0]

    def empty(self) -> bool:
        return not self.body
