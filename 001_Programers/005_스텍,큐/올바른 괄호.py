#while 문을 for 문으로 바꾸기
'''
규칙을 보자
((()))의 경우 첫번째 (의 인덱스는 0, 이에 쌍을 이루는 )의 인덱스는 5
틀린 예를 보면

'''

def solution(s):
    count={"(":0,")":0}
    answer=True
    for x in s:
        count[x]+=1
        if count["("]<count[")"]:
            answer=False
            break
    if not count["("]==count[")"]:
        answer=False
    return answer

solution("())(()")