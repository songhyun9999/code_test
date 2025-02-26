###### dp ################3
import sys
def solution(info, n, m):
    # info [i][0] A -> n개 이상
    # info [i][1] B -> m개 이상
    answer = 0
    size = len(info)
    dp = [[sys.maxsize for i in range(m)]for j in range(size+1)]
    dp[0][0] = 0
    
    for i in range(1,size+1):
        a = info[i-1][0]
        b = info[i-1][1]
        for j in range(m):
            dp[i][j] = min(dp[i][j],dp[i-1][j]+a)
            if j+b < m:
                dp[i][j+b] = min(dp[i][j+b],dp[i-1][j])
    
    answer = sys.maxsize
    for j in range(m):
        answer = min(dp[size][j],answer)
    
    return answer if answer<n else -1

###### 완전 탐색 풀이 ########
# import sys
# def solution(info, n, m):
#     # info [i][0] A -> n개 이상
#     # info [i][1] B -> m개 이상
#     global N,M,SIZE,answer
#     N,M,SIZE,answer = n,m,len(info),sys.maxsize
#     b = 0
#     for x,y in info:
#         b += y
#     if b < m:
#         return 0
    
#     sol(info,0,0,b)
    
#     return answer if answer != sys.maxsize else -1

# def sol(info,depth,a,b):
#     global answer
#     if a>=answer:
#         return
    
#     if a < N and b < M:
#         answer = min(answer,a)
#         return
    
#     if depth == SIZE:
#         return
    
#     sol(info,depth+1,a,b)
#     sol(info,depth+1,a+info[depth][0],b-info[depth][1])