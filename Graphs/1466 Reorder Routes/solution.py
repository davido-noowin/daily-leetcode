from collections import defaultdict

def minReorder(self, n: int, connections: list[list[int]]) -> int:
    visit = set()
    visit.add(0)
    count = [0]
    adj_list = defaultdict(list)
    for u, v in connections:
        adj_list[u].append((v, 1))
        adj_list[v].append((u, 0))

    def dfs(node):
        visit.add(node)

        for neighbor, cost in adj_list[node]:
            if neighbor not in visit:
                visit.add(neighbor)
                count[0] += cost
                dfs(neighbor)
        
    dfs(0)

    return count[0]