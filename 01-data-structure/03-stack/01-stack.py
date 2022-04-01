class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, val) -> None:
        self.top = Node(val, self.top)
        self.print("----- push -----\n")

    def pop(self) -> any:
        val = self.top.val
        self.top = self.top.next
        self.print("----- pop -----\n")
        return val

    def print(self, text="") -> None:
        top = self.top
        arr = []
        cnt = 0
        while top:
            arr.append(top.val)
            top = top.next
            cnt += 1
        log = "\n".join([f"{i}:\t{arr[i]}" for i in range(cnt)])
        print(f"{text}{log}")


if __name__ == "__main__":
    stack = Stack()

    for val in range(1, 6):
        stack.push(val)
