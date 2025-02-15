from collections import defaultdict

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    table = defaultdict(list)

    for string in strs:
        table["".join(sorted(string))].append(string)

    return list(table.values())