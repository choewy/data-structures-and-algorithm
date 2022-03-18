def check(s) -> str:
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                return "NO"

    if stack:
        return "NO"
    else:
        return "YES"


for i in range(int(input())):
    s = input()

    stack = []
    print(check(s))
