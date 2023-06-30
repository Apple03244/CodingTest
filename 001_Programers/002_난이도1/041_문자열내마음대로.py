def solution(strings, n):
    strings.sort(key=lambda x:x[n]+x[:n]+x[n+1:] if len(x)>n else x[n]+x[:n])
    return strings

solution(["sun", "bed", "car"],1)

