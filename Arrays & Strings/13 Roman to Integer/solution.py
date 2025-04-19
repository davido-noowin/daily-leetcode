def romanToInt(s: str) -> int:
    table = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    value = 0
    prev = None
    for i in range(len(s)):
        value += table[s[i]]
        if prev == 'I' and (s[i] == 'V' or s[i] == 'X'):
            value -= 2
        elif prev == 'X' and (s[i] == 'L' or s[i] == 'C'):
            value -= 20
        elif prev == 'C' and (s[i] == 'D' or s[i] == 'M'):
            value -= 200
        prev = s[i]

    return value