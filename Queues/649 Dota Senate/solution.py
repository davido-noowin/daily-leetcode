from collections import deque

def predictPartyVictory(senate: str) -> str:
    radiant = deque()
    dire = deque()

    for index, value in enumerate(senate):
        if value == "R":
            radiant.append(index)
        else:
            dire.append(index)

    while radiant and dire:
        radiant_senator = radiant.popleft()
        dire_senator = dire.popleft()

        if radiant_senator < dire_senator:
            radiant.append(radiant_senator + len(senate))
        else:
            dire.append(dire_senator + len(senate))

    return "Radiant" if radiant else "Dire"