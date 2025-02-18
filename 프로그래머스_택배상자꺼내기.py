def solution(n, w, num):
    box = []
    floor = n//w + 1
    for i in range(floor):
        tmp = []
        for j in range(w):
            idx = (w * i) + j + 1
            if idx > n :
                idx = 0
            if i % 2 == 0: # 왼쪽에서 부터
                tmp.append(idx)
            else : # 오른쪽에서 부터
                tmp.insert(0,idx)
        box.insert(0,tmp)
    
    answer = 0
    tmp = []
    for i in range(w):
        tmp.append(0)
    
    ans = -1
    for items in box:
        i = 0
        #print(items)
        for item in items:    
            # print(tmp)
            if item == 0:
                i += 1
                continue
            tmp[i] +=1
            if item == num:
                ans = i
                break
            i += 1
        if ans != -1:
            break
    
    answer = tmp[ans]
    return answer


# 정답 예제
def solution2(n, w, num):
    warehouse = []
    stack = []

    for i in range(n):
        if len(warehouse) % 2 == 0:
            stack.append(i + 1)
        else:
            stack.insert(0, i + 1)

        if len(stack) == w:
            warehouse.append(stack)
            stack = []

    if stack:
        while len(stack) < w:
            if len(warehouse) % 2 == 0:
                stack.append(0)
            else:
                stack.insert(0, 0)
        warehouse.append(stack)

    for i in range(len(warehouse)):
        for j, value in enumerate(warehouse[i]):
            if value == num:
                if warehouse[-1][j] == 0:
                    return len(warehouse) - i - 1
                return len(warehouse) - i

if __name__ == '__main__':
    n = 13
    w = 3
    num = 6
    print(solution(n,w,num))