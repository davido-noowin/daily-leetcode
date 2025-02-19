def calPoints(operations: list[str]) -> int:
    stack = []

    for op in operations:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "+":
            popped_top = stack.pop()
            added_value = popped_top + stack[-1]
            stack.append(popped_top)
            stack.append(added_value)
        else:
            stack.append(int(op))
        
    return sum(stack)