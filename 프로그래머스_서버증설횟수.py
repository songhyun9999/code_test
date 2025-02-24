def solution(players, m, k):
    now = 0
    check_end = [0] * 24
    total = 0
    for i in range(24):
        now -= check_end[i]
        tmp = players[i]//m
        if  tmp> now:
            total += (tmp-now) # 추가 증설
            if i+k <24:
                check_end[i+k] = (tmp-now)
            now = tmp
            
    answer = total
    return answer