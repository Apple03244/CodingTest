def solution(a,b,n):
    process=[]
    result=[]
    while n>=a:
        process.append(divmod(n,a)[0]*b+divmod(n,a)[1])
        result.append(divmod(n,a)[0]*b)
        n=divmod(n,a)[0]*b+divmod(n,a)[1]

    return sum(result)

solution(3,1,20)

divmod(10,5)