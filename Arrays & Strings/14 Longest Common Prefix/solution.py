def longestCommonPrefix(self, strs: list[str]) -> str:
    i = 0
    smallest_length = float("inf")
    for string in strs:
        smallest_length = min(smallest_length, len(string))


    while i < smallest_length:
        for string in strs:
            if string[i] != strs[0][i]:
                return string[:i]
        i += 1

    return string[:i]