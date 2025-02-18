from itertools import combinations

### combinations 를 활용한 가능한 경우의 수 생성 예제
### 속도 향상을 위해 필요없는 경우를 제거하기 위한 과정이 필요할 수 있음 (속도 제한이 있는 경우)

def solution(n, q, ans):
    answer = 0
    lr = [i for i in range(1,n+1)]
    
    m = len(ans)

    no_matching_idx = list(filter(lambda i : ans[i]==0,range(m)))

    for i in no_matching_idx:
        for j in q[i]:
            try:
                lr.remove(j)
            except:
                pass
    
    ### for else 구문 ###
    # for else 는 for 문이 break 등을 만나지 않고 정상적으로 종료되었을 경우
    # else 안의 구문을 실행하도록 함

    for c in combinations(lr,5):
        for i in range(m):
            cnt = 0
            for j in q[i]:
                if j in c:
                    cnt += 1
            if cnt != ans[i]:
                break
        else:
            answer += 1
    
    return answer



if __name__ == "__main__":
    print(solution(10,[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]],[2, 3, 4, 3, 3]))
