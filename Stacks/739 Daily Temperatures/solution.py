def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    res = [0 for _ in range(len(temperatures))]
    stack = []

    for index, temperature in enumerate(temperatures):
        while stack and temperature > stack[-1][1]:
            stack_index, stack_temperature = stack.pop()
            res[stack_index] = index - stack_index
        stack.append((index, temperature))

    return res
