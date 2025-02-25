from collections import defaultdict

def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True
        
    adj_list = defaultdict(list)
    seen = set()
    seen.add(source)

    for ver, dest in edges:
        adj_list[ver].append(dest)
        adj_list[dest].append(ver)

    def dfs(node):
        if node == destination:
            return True  
            
        for vertex in adj_list[node]:
            if vertex not in seen:
                seen.add(node)
                if dfs(vertex):
                    return True
        return False

    return dfs(source)