from collections import defaultdict,deque

def solution(edges):
    answer = []
    node_map = defaultdict(list)
    for a,b in edges:
        node_map[a].append(b)
        
    c = set()
    for key in node_map.keys():    
        for node in node_map[key]:
            c.add(node)
    
    cnodes = [node for node in node_map.keys() if node not in c]
    cnode = max(cnodes,key=lambda x: len(node_map[x]),default=0)
    
    def identify(node_map,idx):
        visited = set()
        queue = deque([idx])
        n = 0
        edges = 0
        
        # 연결된 노드 전부 찾기
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            n += 1
            for neighbor in node_map[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                edges += 1
        # print(visited,n,edges)
            
        if n == edges:
            return 'donut',visited
        elif n == edges+1:
            return 'stick',visited
        else:
            return '8',visited
    
    donut,stick,eight = 0,0,0
    visited_global = set()
    for idx in node_map[cnode]:
        if idx not in visited_global:
            rtv, visited_local = identify(node_map,idx)
            visited_global.update(visited_local)
            if rtv == 'donut':
                donut += 1
            elif rtv == 'stick':
                stick += 1
            else:
                eight += 1
            
    answer = [cnode,donut,stick,eight]
    return answer


    
print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))