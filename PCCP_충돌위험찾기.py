def solution(points, routes):
    answer = 0
    s_routes = move_robot(points,routes)
    m = -10
    for s_route in s_routes:
        if len(s_route) > m:
            m = len(s_route)
            
    t = [[] for _ in range(m)]
    check = [0 for _ in range(m)]
    check_p = [[] for _ in range(m)]
    
    for s_route in s_routes:
        # print(s_route)
        for i,point in enumerate(s_route):
            if check_point(t[i],point):
                t[i].append(point)
            else:
                if check_point(check_p[i],point):
                    check_p[i].append(point)
                    check[i] += 1
    for p in check:
        if p != 0:
            answer += p    
            
    return answer

def check_point(t,point):
    for i in t:
        if i == point:
            return False
    return True

def move_robot(points,routes):
    s_routes = []
    for route in routes:
        s_route = []
        for i,point in enumerate(route):
            if i == 0:
                s_route.append((points[point-1][0],points[point-1][1]))
                continue
            prev_point = points[route[i-1]-1]
            for p in cal_point(prev_point,points[point-1]):
                s_route.append(p)
        s_routes.append(s_route)
    return s_routes

def cal_point(prev_point,point):
    r = []
    d_y = point[0] - prev_point[0]
    d_x = point[1] - prev_point[1]
    changed = prev_point[0]
    if d_y>0:
        for i in range(1,d_y+1):
            r.append((prev_point[0]+i,prev_point[1]))
            changed = prev_point[0]+i
    else:
        for i in range(1,abs(d_y)+1):
            r.append((prev_point[0]-i,prev_point[1]))
            changed = prev_point[0]-i

    if d_x>0:
        for i in range(1,d_x+1):
            r.append((changed,prev_point[1]+i))
    else:
        for i in range(1,abs(d_x)+1):
            r.append((changed,prev_point[1]-i))
    return r
    
# print(solution([[1, 1], [1, 3], [1, 4], [3, 3]], [[1, 3], [3, 2], [4, 2]]))