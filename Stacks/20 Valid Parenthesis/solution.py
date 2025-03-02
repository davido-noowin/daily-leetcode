def isValid(s: str) -> bool:
    valid = {'{' : '}', '(' : ')', '[' : ']'}
    stack = []

    for char in s:
        if char in valid:
            stack.append(char)
        else:
            if not stack or valid[stack[-1]] != char:
                return False
            stack.pop()

    return len(stack) == 0