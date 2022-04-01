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

    def last(self) -> any:
        if self.top:
            val = self.top.val
            return val
        else:
            None

    def find(self, val) -> bool:
        if self.top:
            top = self.top
            while top:
                if val == top.val:
                    return True
                top = top.next
        return False

    def all(self) -> bool:
        vals = []
        if self.top:
            top = self.top
            while top:
                vals.append(top.val)
                top = top.next
        vals.reverse()
        return vals


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = {c: s.count(c) for c in set(s)}
        stack = Stack()
        for c in s:
            counter[c] -= 1
            if stack.find(c):
                continue
            if stack.top:
                while stack.top:
                    last = stack.last()
                    if counter[last] == 0:
                        break
                    if c > last:
                        break
                    stack.pop()
            stack.push(c)
        return ''.join(stack.all())


if __name__ == "__main__":
    test_case = [
        {"input": "ecbacba", "expected": "eacb"},
        {"input": "cbacdcbc", "expected": "acdb"},
        {"input": "bcabc", "expected": "abc"},
    ]

    def test():
        for case in test_case:
            i = case["input"]
            e = case["expected"]
            o = solution.removeDuplicateLetters(i)

            if o != e:
                case["result"] = False
                case["output"] = o
                return pprint(case)

        print(True)

    solution = Solution()
    test()
