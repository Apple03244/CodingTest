def solution(s):
    return s[len(s)//2] if len(s)%2 else s[len(s)//2-1:len(s)//2+1]

"12345"[2]
"123456"[3:5]
"1234"[1:3]