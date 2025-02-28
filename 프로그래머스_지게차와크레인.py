#      방식	                 스택 사용 여부	               메모리 사용량	       실행 속도
# 재귀 (Recursion)	✅ 함수 호출마다 스택 프레임 생성       O(n) (많음)	    느림 (재귀 호출 오버헤드)
# 반복문 (Iteration)	❌ 스택 사용 안 함	              O(1) (적음)	           빠름
# 재귀 사용시 메모리 터져서 recursion error 발생 가능
def solution(storage, requests):
    global n, m, stack, visited
    n = len(storage)
    m = len(storage[0])
    storage = [list(row) for row in storage]
    for request in requests:
        if len(request) == 2: # 크레인 출고 요청
            for i in range(n):
                for j in range(m):
                    if str(storage[i][j]) == request[0]:
                        storage[i][j] = -1 # 해당 택배를 꺼냄
        else: # 지게차 출고 요청
            global checked_points
            tmp_storage = [[-1 for _ in range(m+2)]for _ in range(n+2)]
            for i in range(n):
                for j in range(m):
                    tmp_storage[i+1][j+1] = storage[i][j] 
            stack = []
            visited = set()
            stack.append((0,0))
            visited.add((0,0))
            checked_points = []
            while True:
                ch = dfs(tmp_storage,request)
                if ch==0:
                    break
            for i,j in checked_points:
                if 0 <= i-1 < n and 0 <= j-1 < m:
                    storage[i-1][j-1] = -1
            
    answer = n*m
    for i in range(n):
        for j in range(m):
            if storage[i][j] == -1:
                answer -= 1
    
    print(answer)
    
    return answer

def dfs(storage,request):
    global stack,checked_points
    if len(stack) == 0:
        return 0
    n = len(storage)
    m = len(storage[0])
    
    i,j = stack.pop()
    directions = [(0,1),(1,0),(0,-1),(-1,0)] # 오른쪽, 아래, 왼쪽, 위
    for di, dj in directions:
        ni, nj = i+di, j+dj
        if 0<= ni< n and 0<= nj< m:
            if (ni,nj) not in visited and storage[ni][nj] == -1:
                stack.append((ni,nj))
                visited.add((ni,nj))
    
    # 정답 체크
    for di, dj in directions:
        ni, nj = i+di, j+dj
        if 0<= ni< n and 0<= nj< m:
            if str(storage[ni][nj]) == request and (ni,nj) not in checked_points:
                checked_points.append((ni,nj))
    
    
    
# solution(["AAA","BAB","AAA"],["A"])