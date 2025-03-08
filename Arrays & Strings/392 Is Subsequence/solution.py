def isSubsequence(self, s: str, t: str) -> bool:
    if s == '':
        return True

    if len(s) > len(t):
        return False

    s_pointer = 0
    for i in range(len(t)):
        if s[s_pointer] == t[i]:
            if s_pointer == len(s) - 1:
                return True
            s_pointer += 1

    return False