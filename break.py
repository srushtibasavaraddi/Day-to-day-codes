t,s=map(int,input().split())
while(t):
    t-=1
    n=int(input())
    arr=[int(n) for n in input().split()]
    brr=[int(n) for n in input().split()]
    arr.sort()
    brr.sort()
    # print(arr,brr)
    table=set()
    f=0
    for i in range(n):
        if(i>0):
            if not(arr[i] in table):
                f=1

        if(arr[i]>=brr[i]):
            f=1
        else:
            table.add(arr[i])
            table.add(brr[i])
        
        # print(table)  

        if(f==1):
            break
    if(f==1):
        print("NO")
    else:
        print("YES")