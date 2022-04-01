#교수님
def solution01(clothes):

    clothesTypeMap = {}

    for clothe, clothesType in clothes :
        clothesTypeMap[clothesType] = clothesTypeMap.get(clothesType, 0) +1
    answer = 1
    for clothesType in clothesTypeMap:
            answer *= (clothesTypeMap[clothesType]+1)

    return answer-1



def solution02(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1




if __name__ == "__main__" :

    map = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution01(clothes))


