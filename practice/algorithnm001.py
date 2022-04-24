import math

#순서대로 정렬되어 있음을 가정
su=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,1000]

#최대 값
max_su = su[len(su)-1]

for i in su:
    print("i : ", i, " max_su : ", max_su)
    if i*i  < max_su:

        for j in su:

            if j>i and j%i==0:
                su.remove(j)


print(su)