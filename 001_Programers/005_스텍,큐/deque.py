from collections import deque
def solution(priorities, location):
    answer = 0
    mydoc = [0 for _ in range(len(priorities))]
    mydoc[location] = 1
    queue = deque(priorities)
    while True:
        if not mydoc or max(mydoc) == 0:
            break
        if max(queue) == queue[0]:
            queue.popleft()
            del mydoc[0]
            answer += 1
        else:
            queue.append(queue[0])
            mydoc.append(mydoc[0])
            queue.popleft()
            del mydoc[0]
    return answer