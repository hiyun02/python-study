#교수님 풀이
def solution01(participant, completion) :

    tmp=0

    dic={}

    for p in participant:

        dic[hash(p)] = p

        tmp +=int(hash(p))

    for com in completion:

        tmp -= hash(com)

    return dic[tmp]

#내 풀이
def solution02(participant, completion) :
    participant.sort
    completion.sort

    i=0
    while completion[i]==participant[i] :
            i=i+1
            if i==completion.length :
                return participant[completion.length]
    return participant[i]

#테스트 로직
if __name__ == "__main__":
    a = ["mislav", "stanko", "mislav", "ana"]
    b = ["stanko", "ana", "mislav"]

    print(solution01(a, b))
    print(solution02(a, b))

