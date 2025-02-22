def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    start = 0
    length = 0
        
    for end in range(len(s)):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        length = max(length, end - start + 1)

    return length