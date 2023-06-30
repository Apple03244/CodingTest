'''
def solution(park, routes):
    temp={'H':0,'W':0} #세로,가로
    map_size={'H': len(park)-1, 'W': len(park[0])-1}
    def rout(x):
        id_x = x.split()
        idx, n = id_x[0], int(id_x[1])
        temp = {"N": ["H",-1,n], 'S': ["H",1,n], 'E': ["W",1,n], 'W': ["W",-1,n]}
        return temp[idx] # 인덱스,방향,횟수

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=="S":
                temp["H"]=i
                temp["W"]=j
                break
            # 초기값 설정
    sm=temp
    for x in routes:
        if





    return temp
'''



