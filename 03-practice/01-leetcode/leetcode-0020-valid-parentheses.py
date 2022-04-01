from pprint import pprint


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, val) -> None:
        self.top = Node(val, self.top)

    def pop(self) -> any:
        if self.top:
            val = self.top.val
            self.top = self.top.next
            return val
        else:
            None


class Solution:
    def isValid(self, s: str) -> bool:

        openers = "[{("
        closers = "]})"

        if s[0] in closers:
            return False

        if s[-1] in openers:
            return False

        hashtable = {closers[i]: openers[i] for i in range(len(closers))}
        stack = Stack()
        for c in s:
            if c in openers:
                stack.push(c)
            else:
                opener = stack.pop()

                if hashtable[c] != opener:
                    return False

        return not stack.top


if __name__ == "__main__":
    test_case = [
        {"input": "[])", "expected": False},
        {"input": "()", "expected": True},
        {"input": "([]", "expected": False},
    ]

    def test():
        for case in test_case:
            i = case["input"]
            e = case["expected"]
            o = solution.isValid(i)

            if o != e:
                case["result"] = False
                case["output"] = o
                return pprint(case)

        print(True)

    solution = Solution()
    test()
