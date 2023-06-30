def solution(n):
    rule=lambda x:"박" if x%2 else "수"
    return "".join([rule(i) for i in range(n)])

solution(3)