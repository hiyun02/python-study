arr = list(map(int,input().split()))
n=int(input())
arr[2]+=n
if arr[2]>59 :
    arr[1]+=arr[2]/60
    arr[2]%=60
if arr[1]>59 :
    arr[0]+=arr[1]/60
    arr[1]%=60
if arr[0]>23 :
    arr[0]%=24

print('%d %d %d' %(arr[0], arr[1], arr[2]))
