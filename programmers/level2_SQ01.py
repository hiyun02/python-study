from collections import deque
def solution(priorities, location):

    answer = 0

    myDeque = deque([(v,i) for i,v in enumerate(priorities)])

    while myDeque:

        firstData = myDeque.popleft()

        if myDeque and max(myDeque)[0] > firstData[0] :
            myDeque.append(firstData)
        else:
            answer+=1
            if location == firstData[1]:
                break

    return answer