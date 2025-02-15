def mergeAlternately(word1: str, word2: str) -> str:
    string = []
    i = 0
    while i < len(word1) and i < len(word2):
        string.append(word1[i])
        string.append(word2[i])
        i += 1

    string.append(word1[i:])
    string.append(word2[i:])

    return "".join(string)