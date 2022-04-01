# sorted 함수를 이용한 풀이
def solution01(array, commands) :
    return [sorted(  array[ i[0]-1 : i[1] ]  )[i[2]-1] for i in commands]


# 교수님 풀이
def solution02(array, commands) :
    answer = []

    cmd_length = len(commands)

    for i in range(cmd_length):

        arr_list = array[commands[i][0]-1 : commands[i][1]]

        arr_list.sort()

        answer.append(arr_list[commands[i][2]-1])

    return answer


#테스트용 예제 출력
if __name__== "__main__" :

    input_A = [1, 5, 2, 6, 3, 7, 4]
    input_B = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    result = solution02(input_A,input_B)

    for i in result :
        print(i, end=' ')