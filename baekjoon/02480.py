award = 0
arr = list(map(int,input().split()))

if arr[0] == arr[1] :
    if arr[0] == arr[2] :

        award = 10000+ arr[0]*1000
    else :
        award = 1000+arr[0]*100
else :
    if arr[1] == arr[2] :
        award = 1000+arr[1]*100
    else :
        if arr[2] == arr[0] :
            award = 1000+arr[2]*100
        else :
            award = max(arr) * 100
print(award)