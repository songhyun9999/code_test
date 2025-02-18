def solution(schedules, timelogs, startday):
    answer = 0
    i = 0
    check = 0
    n = len(schedules)
    
    for i in range(n):
        for j in range(7):
            ch = True
            idx = (j+startday)%7
            if idx == 0:
                idx = 7
            # print(i,idx)
            if idx == 6:
                ch = False
            elif idx == 7:
                ch = False
            
            if ch:
                t2 = int(str(timelogs[i][j])[:-2])*60
                t1 = int(str(schedules[i])[:-2])*60

                t2 = t2 + int(str(timelogs[i][j])[-2:])
                t1 = t1 + int(str(schedules[i])[-2:])

                # print(t2,t1)

                if (t2-t1)>10:
                    check += 1
                    break
    
    answer = n-check
    return answer



if __name__ == '__main__':
    a =[730, 855, 700, 720]
    b = [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]
    c = 1
    print(solution(a,b,c))