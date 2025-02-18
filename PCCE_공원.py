def solution(mats, park):
    answer = -1
    mats.sort(reverse = True)
    for s in mats:
        if checkMat(s,park):
            answer = s
            break
    return answer

def checkMat(s, park):
    rows = len(park)
    cols = len(park[0])
    
    for i in range(rows - s + 1):
        for j in range(cols - s + 1):
            if isSquareEmpty(i, j, s, park):  
                return True  
    return False  

def isSquareEmpty(x, y, s, park):
    for i in range(s):
        for j in range(s):
            if park[x + i][y + j] != '-1':  
                return False  
    return True  

# def checkMat(s, park):
#     for i in range(len(park) - s + 1):  # 가능한 행 범위 설정
#         ch = True
#         for j in range(len(park[i]) - s + 1):  # 가능한 열 범위 설정
#             ch = True
#             for k in range(s):  # s x s 크기의 정사각형 검사
#                 for q in range(s):
#                     if park[i + k][j + q] != '-1':  # 하나라도 '-1'이 아니면 실패
#                         ch = False
#                 if ch == False:
#                     break
#             else:
#                 return True

#     return False

if __name__ == '__main__':
    print(solution([2],[["-1", "A", "-1"],["-1", "-1", "-1"],["A", "-1", "-1"]]))