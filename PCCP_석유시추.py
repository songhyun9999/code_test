from collections import defaultdict

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    visited = set()
    oil_cols = defaultdict(list)
    
    def dfs(x,y):
        move = [(1,0),(-1,0),(0,1),(0,-1)] # 아래 위 오른쪽 왼쪽
        stack = []
        visited_tmp = []
        count = 1
        stack.append((x,y))
        visited.add((x,y))
        visited_tmp.append((x,y))
        while stack:
            i,j = stack.pop()
            for dx,dy in move:
                nx, ny = i+dx, j+dy
                if 0<=nx<n and 0<=ny<m:
                    if (nx,ny) not in visited and land[nx][ny] != 0:
                        count += 1
                        visited.add((nx,ny))
                        visited_tmp.append((nx,ny))
                        stack.append((nx,ny))
                        
        check = set()
        for _,j in visited_tmp:
            if j not in check:
                oil_cols[j].append(count)
                check.add(j)
            
        
    for j in range(m):
        for i in range(n):
            if (i,j) not in visited and land[i][j]!=0:
                dfs(i,j)
    
    for values in oil_cols.values():
        answer = max(sum(values),answer)        
             
    
    return answer



prob1 = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
prob2 = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]

print(solution(prob2))