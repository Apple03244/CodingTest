def solution(x,y):
    #naming
    name_list=list(zip(range(len(x)),x,y))
    name_list.sort(key=lambda x:x[2],reverse=True)
    #dict 만들기 [고유번호],합
    final=dict.fromkeys(x)
    for x in final:
        final[x]=[[y[0] for y in name_list if y[1]==x],sum([y[2] for y in name_list if y[1]==x])]
    #랭킹
    lank=[(x,final[x][-1]) for x in final]
    lank.sort(key=lambda x:x[1],reverse=True)
    #추출
    answer=[]
    for x in lank:
        answer+=final[x[0]][0][:2]
    return answer

A=[1,2,3]
A[:4]

A=solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])
A