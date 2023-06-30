def solution(n):
    rule=lambda x:x//2 if x%2==0 else x*3+1
    count=0
    while True:
        if n==1:
            break
        else:
            n=rule(n)
            count+=1
            if count==500:
                count=-1
                break
    return count

solution(6)