import numpy as np
def solution(n, arr1, arr2): #n:한변의 크기
    def chagebase(x): #y:base
        result=[]
        while x>=2:
            result.append(divmod(x,2)[1])
            x=divmod(x,2)[0]
        result.append(x)
        return result
    a1=[chagebase(x)+[0 for i in range(n-len(chagebase(x)))] for x in arr1]
    a2=[chagebase(x)+[0 for i in range(n-len(chagebase(x)))] for x in arr2]
    def key(x=list): #변환함수
        dic={1:"#",0:" ",2:"#"}
        rs=x[::-1]
        return "".join(list(map(lambda x:dic[x],rs)))
    A=np.array([[1,2,3],[3,4,5]])
    result=list(map(key,list(np.array(a1)+np.array(a2))))
    return result

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])









'''
a,sum=0,0
while a<1000:
    a+=1
    if not a%2:
        continue
    sum+=a
sum
a=[i for i in range(1001)]

[i for i in]

sum([i for i in range(1001) if i%2==1])'''

'''def chagebase(x,y): #y:base
        result=[]
        while x>=y:
            result.append(divmod(x,y)[1])
            x=divmod(x,y)[0]
        result.append(x)
        return result
    '''
