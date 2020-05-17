#min of arr
import math
n=10
sq=int(math.sqrt(n))
arr=[2,3,4,6,32,12,12,3,34,18]
def build(arr,n):
    sqarr=[]
    for i in range(sq):
        m=99999
        for j in range(sq):
            if(arr[sq*i+j]<m):
                m=arr[sq*i+j]
        sqarr.append(m)

    if(n>sq*sq):
        m=99999
        for i in range(sq*sq,n):
            if(arr[i]<m):
                m=arr[i]
            sqarr.append(m)
    return sqarr
sqarr=build(arr,n)
def query(l,r):
    m=99999
    while(l%sq!=0):
        if(arr[l]<m):
            m=arr[l]
        l+=1
    while(l+sq<=r):
        if(sqarr[l//sq]<m):
            m=arr[l//sq]
        l+=sq
    while(l!=r):
        if(arr[l]<m):
            m=arr[l]
        l+=1
    return m
print(build(arr,n))
print(query(5,8))