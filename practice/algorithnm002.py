import math

def numberCheck(num):

    if num ==0 or num ==1 :
        return False
    else:

        #2부터 입력받은 숫자의 제곱값까지 반복
        #입력받은 값이 10이면 100번 반복
        for i in range(2, int(math.sqrt(num))+1):
            print(i)
            if num % i ==0:
                return False
    return False

print(numberCheck(10))
print(numberCheck(49))