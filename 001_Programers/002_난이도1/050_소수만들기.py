def solution(nums):
    cand=[]
    prime = lambda x: 1 if all([bool(x % i) for i in range(2, x)]) else 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for z in range(j+1,len(nums)):
                cand.append([nums[i],nums[j],nums[z]])
    return sum(list(map(prime,list(map(sum,cand)))))
solution([1,2,3,4])

prime(7)
int(True)