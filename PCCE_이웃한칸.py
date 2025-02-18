def solution(board, h, w):
    answer = 0
    color = board[h][w]
    d = [1,-1]
    for i in d:
        if len(board[h]) > (w+i) and (w+i)>=0:
            if board[h][w+i] == color:
                answer += 1
        if len(board) > (h+i) and (h+i)>=0:
            if board[h+i][w] == color:
                answer += 1
    
    return answer