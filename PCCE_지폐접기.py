def solution(wallet, bill):
    answer = 0
    w,h = wallet[0],wallet[1]
    b_w,b_h = bill[0],bill[1]

    while check(w,h,b_w,b_h):
        b_w, b_h = fold(b_w,b_h)
        answer += 1
    return answer

def fold(w,h):
    if w>=h:
        return w//2, h
    else:
        return w, h//2
    
def check(w,h,b_w,b_h):
    if w >= b_w and h>=b_h:
        return False
    if w >= b_h and h>=b_w: # 90도 회전
        return False
    
    return True