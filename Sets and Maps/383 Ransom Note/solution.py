def canConstruct(ransomNote: str, magazine: str) -> bool:
    table = {}
    for item in magazine:
        table[item] = table.get(item, 0) + 1

    for letter in ransomNote:
        if table.get(letter, 0) <= 0:
            return False
        table[letter] -= 1

    return True