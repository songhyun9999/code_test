def solution(bandage, health, attacks):
    answer = 0
    t,x,y = bandage
    max_health = health
    d_t = dict()
    for a_t,d in attacks:
        d_t[a_t] = d
    
    band_t = 0
    for i in range(1,1001):
        check_t = d_t.keys()
        band_t += 1
        if len(check_t) <= 0:
            break
        
        if i in check_t:            
            health = health - d_t[i]
            del d_t[i]
            if health <= 0 :
                return -1
            band_t = 0
            continue
        
        health += x
        if band_t == t:
            health += y
            band_t = 0
        
        if health > max_health:
            health = max_health
        
    answer = health
        
    
    return answer
    