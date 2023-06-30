def solution(n):
    def base_3(x):
        result=[]
        while x>=3:
            result.append(divmod(x,3)[1])
            x=divmod(x,3)[0]
            print(x,result)
        result.append(x)
        return result
    return int("".join(list(map(str,base_3(n)))),base=3)


solution(45)

    base_3(18)

a=[1,2,3,4,5]
a.extend([6,7])
a[::-1]
"".join(a)