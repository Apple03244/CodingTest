def solution(x,y):
    dic=dict(zip([3,4,5,6,0,1,2],['SUN','MON','TUE','WED','THU','FRI','SAT']))
    num=dict(zip(range(1,13),[31,29,31,30,31,30,31,31,30,31,30,31]))
    day=0
    if x==1:
        day=dic[y%7]
    else:
        day=dic[(sum([num[i] for i in range(1,x)])+y)%7]
    return day

solution(5,24)
sum(num)
A=[(sum([num[i] for i in range(1,5)]
num={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
sum(num.values())