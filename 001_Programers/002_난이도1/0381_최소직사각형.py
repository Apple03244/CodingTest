solution([[60, 50], [30, 70], [60, 30], [80, 40]])

def solution(sizes):
    #기본값 설정
    temp=dict.fromkeys(["r","w"])
    temp["r"]=sizes[0][0]
    temp["w"]=sizes[0][1]
    size=lambda x:x["r"]*x["w"]
    for x in sizes: #작은 값을 선택할거얌
        if max(temp["r"],x[0])*max(temp["w"],x[1])<=max(temp["w"],x[0])*max(temp["r"],x[1]):
            temp["r"]=max(temp["r"],x[0])
            temp["w"]=max(temp["w"],x[1])
        else:
            temp["r"]=max(temp["r"],x[1])
            temp["w"]=max(temp["w"],x[0])
    return size(temp)



    '''def upd(x): #업데이트
        if temp["r"]<=x[0]:
            temp["r"]=x[0]
        if temp["w"]<=x[1]:
            temp["w"]=x[1]
        return temp
    
    return temp
    
    def v(x):
        ori=size(temp)
        ob1=upd(x)
        ob2=upd(x[::-1])
        
    '''


    a=1
    while a<=1000:
        print(f'{a}')
        a+=1