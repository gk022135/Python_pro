#include<stdio.h>
int main()
{
    int arr[]={1,23,45,6,7,2,67,88,9,4,7},i,max,min,j,k;
    
    for(i=0;i<=10;i++)
    {
        if(arr[i]>arr[0])
         arr[0]=arr[i];
         max=arr[0];
    }
    printf("max=%d",max);
    printf('\n');
for(i=0;i<=10;i++)
    {
        if(arr[i]>arr[0])
         min=arr[0];
        else
         min=arr[i];
    }
printf("max=%d",min);
printf('\n');

for(i=1;i<11;i++)
    {
        printf("%d,",arr[i]);
    }
   
    
}