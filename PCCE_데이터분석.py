def solution(data, ext, val_ext, sort_by):
    # data [["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]]
    # ext,sort_by "code", "date", "maximum", "remain"
    answer = []
    # 데이터 추가
    if ext == 'code':
        for (code,date,maxim,remain) in data:
            if code < val_ext:
                answer.append(list((code,date,maxim,remain)))
    elif ext == 'date':
        for (code,date,maxim,remain) in data:
            if date < val_ext:
                answer.append(list((code,date,maxim,remain)))
    elif ext == 'maximum':
        for (code,date,maxim,remain) in data:
            if maxim < val_ext:
                answer.append(list((code,date,maxim,remain)))
    elif ext == 'remain':
        for (code,date,maxim,remain) in data:
            if remain < val_ext:
                answer.append(list((code,date,maxim,remain)))
                
    # 정렬 
    st = -1
    if sort_by == 'code':
        st = 0
        for i in range(len(answer)-1):
            for j in range(i+1,len(answer)):
                if answer[i][st] > answer[j][st]:
                    answer[i],answer[j] = answer[j],answer[i]
    elif sort_by == 'date':
        st = 1
        for i in range(len(answer)-1):
            for j in range(i+1,len(answer)):
                if answer[i][st] > answer[j][st]:
                    answer[i],answer[j] = answer[j],answer[i]
    elif sort_by == 'maximum':
        st = 2
        for i in range(len(answer)-1):
            for j in range(i+1,len(answer)):
                if answer[i][st] > answer[j][st]:
                    answer[i],answer[j] = answer[j],answer[i]
    elif sort_by == 'remain':
        st = 3
        for i in range(len(answer)-1):
            for j in range(i+1,len(answer)):
                if answer[i][st] > answer[j][st]:
                    answer[i],answer[j] = answer[j],answer[i]
    
    return answer

if __name__ == '__main__':
    print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],"date",20300501,	"remain"))