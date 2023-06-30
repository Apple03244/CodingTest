def solution(absolutes, signs):
    rule=lambda x:x[0]*int(x[1]) if x[1] else x[0]*(-1)
    num_list=list(zip(absolutes,signs))
    return sum(map(rule,num_list))
