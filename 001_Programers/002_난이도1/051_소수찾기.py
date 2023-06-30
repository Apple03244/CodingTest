# def solution(n):
#     prime = lambda x: 1 if all([bool(x % i) for i in range(2, x)]) else 0
#     result=0
#     if n==2:
#         return 1
#     elif n==1:
#         return 0
#     else:
#         for num in range(3,n+1):
#             result+=prime(num)
#         return result+1 #2를 계산하지 않았기 때문

#효율성이 안나옴
def solution(x):
    prime = lambda x: 1 if all([bool(x % i) for i in range(2, x)]) else 0
    ls=list(range(x,1,-1))
    result=0
    for x in ls:
        result+=prime(x)
    return result
#
def solution(n):
    ls=list(range(n,1,-1))
    result=[]
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]%ls[j]==0:
                result.append(ls[i])
                break
    return n-1-len(result)






solution(10)
import math
dir(math)
def solution(n):
    prime = lambda x: 1 if all([x % i for i in range(2, x)]) else 0
    return sum(map(prime,range(2,n+1)))

def solution(n):
    #filter 써보자
    m=2
    numlist=list(range(2,n+1))
    result=[]
    while True:
        result.append(m)
        numlist=list(filter(lambda x:x%m!=0,numlist))
        print(numlist,m,result)
        if not numlist:
            break
        else:
            m=numlist[0]
    return len(result)
solution(5)


a=[1,2,3,4]
a.de(10)

#진짜 마지막
import math
dir(math)
def solution(n):
    prime_set=[2]
    ls=[x for x in list(range(2,n+1))]
    while True:
        ls=[x for x in ls if x%prime_set[-1]]
        for x in ls:
            if all(map(lambda i:x%i,[i for i in prime_set if i<=x**(1/2)])):
                prime_set.append(x)
                break
        #언제까지 할거냥
        #시벌...


    prime_set=[] #소수 리스트
    def prime(x): #소수 확인
        if all(map(lambda y:x*y,[i for i in prime_set if i<=pow(x,1/2)])):
            prime_set.append(x)

def solution(n):
    prime_set=[] #소수 리스트
    Z=list(range(2,n+1))
    while Z:
        for x in Z:
            if all(map(lambda y:x*y,[i for i in prime_set if i<=pow(x,1/2)])):
                prime_set.append(x)
                Z=list(filter(lambda num:num%x,Z))
                #print(Z)
                break
    return prime_set

def solution(n):
    prime=[]
    test=list(range(2,n+1))



dic={}
for a in ['lee','kim','park']:
    dic[a]=a

#zip
dic=dict(zip(['lee','kim','park'],[1,2,3]))
dict(enumerate(['lee','kim','park']))
a=10
a