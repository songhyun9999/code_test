def solution(video_len, pos, op_start, op_end, commands):
    mm , ss = pos.split(':')
    opst_mm, opst_ss = op_start.split(':')
    oped_mm, oped_ss = op_end.split(':')

    

    for command in commands:
        pos = mm + ':'+ss
        if checkOp(pos,op_start,op_end):
            mm = oped_mm
            ss = oped_ss 
        
        if command == 'next':
            if int(ss) + 10 < 60:
                if checkEnd(mm + ':'+str(int(ss)+10),video_len):
                    mm, ss = video_len.split(':')
                else :
                    ss = str(int(ss) + 10)
            else :
                if checkEnd(str(int(mm)+1) + ':'+str(int(ss)+10-60),video_len):
                    mm, ss = video_len.split(':')
                else:
                    ss = str(int(ss) + 10-60)
                    mm = str(int(mm)+1)
        elif command == 'prev':
            if int(ss) - 10 >= 0:
                ss = str(int(ss) - 10)
            else :
                if int(mm)-1 < 0:
                    ss = '00'
                    mm = '00'
                else :
                    ss = str(int(ss) - 10+60)
                    mm = str(int(mm)-1)
        mm,ss = checkLen(mm,ss)
    pos = mm + ':'+ss
    if checkOp(pos,op_start,op_end):
        mm = oped_mm
        ss = oped_ss

    answer = mm +':'+ss
    return answer

def checkLen(mm,ss):
    if len(mm) == 1:
        mm = '0'+ mm
    if len(ss) == 1:
        ss = '0' + ss 
    return mm,ss

def checkOp(pos,op_start,op_end):
    mm , ss = pos.split(':')
    opst_mm, opst_ss = op_start.split(':')
    oped_mm, oped_ss = op_end.split(':')

    if int(opst_mm) <= int(mm) and int(mm) <= int(oped_mm):
        if int(opst_mm) == int(oped_mm):
            if int(ss) <= int(oped_ss) and int(opst_ss) <= int(ss):
                return True
            else:
                return False
        if int(opst_mm) == int(mm):
            if int(opst_ss) <= int(ss):
                return True
            else:
                return False
        if int(mm) == int(oped_mm):
            if int(ss) <= int(oped_ss):
                return True
            else:
                return False
        return True

    return False

def checkEnd(pos,video_len):
    mm , ss = pos.split(':')
    end_mm, end_ss = video_len.split(':')

    if int(mm) > int(end_mm):
        return True

    if int(mm) == int(end_mm):
        if int(ss) >= int(end_ss):
            return True

    return False


if __name__ == '__main__':
    print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))