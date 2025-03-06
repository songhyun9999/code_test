def solution(diffs, times, limit):
    low = 1
    high = max(diffs)
    t = 0
    ch = -1
    while high >= low:
        level = (high + low)//2
        t = 0
        for i,diff in enumerate(diffs):
            if diff > level:
                t += time_spend(times,i) * (diff-level)
            t += times[i]
                
            if t>limit :
                ch = -1
                break
            else:
                ch = 0
                
        if ch == 0:
            high = level - 1
        else:
            low = level + 1
    
    answer = low
    return answer

def time_spend(times, idx):
    if idx>0:
        t = times[idx] + times[idx-1]
    else:
        t = times[idx]
    return t       

# print(solution([1, 5, 3], [2, 4, 7], 30))