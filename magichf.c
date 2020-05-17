#include <stdio.h>
#include <stdlib.h>

int main()
{
    int T;
    int no_boxes;
    int coin_box;
    int swaps;
    int i,j;
    int swap1,swap2;
    scanf("%d",&T);
    for(i=0; i<T; i++)
    {
        scanf("%d%d%d",&no_boxes,&coin_box,&swaps);
        {
            for(j=0;j<swaps;j++)
            {
                scanf("%d%d",&swap1,&swap2);
                if(swap1==coin_box)
                    coin_box=swap2;
                else if(swap2==coin_box)
                    coin_box=swap1;
            }
        }
        printf("\n%d",coin_box);
    }
}
