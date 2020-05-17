#include <stdio.h>

int main(void)
{ 
 int coin[1000],n,type[1000],i,min1=100000,min2=100000,min3=100000;
 scanf("%d",&n);
 for(i=0;i<n;i++)
 {
   scanf("%d",&coin[i]);
 }
  printf("\n");
 
 for(i=0;i<n;i++)
 {
     scanf("%d",&type[i]);
 }	
 for(i=0;i<n;i++)
 {
    if(type[i]==1)
    { 
        if(coin[i]<min1)
         min1=coin[i];
    }
    else if(type[i]==2)
    {    
        if(coin[i]<min2)
         min2=coin[i];
    }
    else
        {    
        if(coin[i]<min3)
         min3=coin[i];
        }
 }
 
 if(min1+min2<min3)
 printf("%d",min1+min2);
 
 else
 printf("%d",min3);
    
    
}

