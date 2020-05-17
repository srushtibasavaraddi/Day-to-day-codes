#include <stdio.h>
#include <stdlib.h>
#include<math.h>

static int n;

void tri(int B)
{
    if(B<4)
        return;
    else
    {
        n=n+ (((B-2)/2)*2) -1;
        tri(B-4);
           
    }
    
}
int main()
{
    int t;
    scanf("%d",&t);
    int i,x;
    int arr[1000];
    for(i=0;i<t;i++)
    {
        scanf("%d",&x);
        arr[i]=x;
        
    }
    for(i=0;i<t;i++)
    {
        n=0;
        tri(arr[i]);
        printf("%d\n",n);
    }
    
    return 0;
}
