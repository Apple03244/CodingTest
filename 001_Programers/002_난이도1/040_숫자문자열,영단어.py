def solution(s):
    key = dict.fromkeys(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    i=0
    for x in key:
        key[x]=i
        i+=1
    key
    while True:
        if s.isnumeric():
            break
        else:
            for x in key:
                s=s.replace(x[0],x[1])
    return s

#우씨
def solution(s):
    key={'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    result=None
    for x in key:
        if x in s:
            s=s.replace(x,str(key[x]))
    return s



solution("one4seveneight")
A="1bdc"
"1b" in A
A=A.replace("1","one")
A

A[0].isnumeric()
"123".replace("0","one")
