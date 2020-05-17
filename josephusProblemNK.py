def josephus(n,k):
    res=0
    for i in range(1,n+1):
        res=(res+k)%i
        # print(res+1)
    return res+1
print(josephus(6,3))