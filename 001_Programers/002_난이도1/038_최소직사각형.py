def solution(sizes):
    def base_2(x):
        result=[]
        while x>=2:
            result.append(divmod(x,2)[1])
            x=divmod(x,2)[0]
        result.append(x)
        return result
    col=list(map(base_2,[i for i in range(pow(2,len(sizes)))]))
    for x in col:
        if len(x)<4:
            x.extend([0 for i in range(4-len(x))])
    change=lambda x,y : y[::-1] if x==1 else y #x==1일때만 바꾸기
    answer=[[change(y[0],y[1]) for y in list(zip(x,sizes))] for x in col]
    size=lambda x: max([i[0] for i in x])*max([i[1] for i in x])
    return min([size(j) for j in answer])



solution([[60, 50], [30, 70], [60, 30], [80, 40]]	)
'''
    print("집에 가")