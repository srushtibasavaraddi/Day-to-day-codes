n=int(input())
arr=[int(n) for n in input().split()]
def kadane():
    tmax=0
    m=-10000000
    for i in range(n):
        tmax=tmax+arr[i]
        if(m<tmax):
            m=tmax
        if(tmax<0):
            tmax=0
    print(m)
kadane()
    
