#교수님 풀이
def solution01(phone_book):
    phone_book.sort()

    answer = True

    phone_length = len(phone_book)

    for i in range(phone_length - 1):

        if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
            answer = False

            break

    return answer


#내 풀이
def solution02(phone_book):

        answer = True

        dic = {}

        for phone_number in phone_book:
            dic[phone_number] = 1

        for phone_number in phone_book:
            jubdu = ""
            
            for number in phone_number:

                jubdu += number

                if jubdu in dic and jubdu != phone_number:
                    answer = False

        return answer


#테스트 로직
if __name__ == "__main__" :

    input = ["119", "97674223", "1195524421"]

    print(solution01(input))
    print(solution02(input))