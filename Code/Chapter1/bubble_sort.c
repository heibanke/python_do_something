/**********************
copyRight by heibanke
***********************/

#include <stdio.h>

void bubble_sort(int nums[],int length){
    int temp;
    for(int i=1;i<length;i++){
        for(int j=0;j<length-i;j++)
        {
            if(nums[j]>nums[j+1]){
                temp=nums[j];
                nums[j]=nums[j+1];
                nums[j+1]=temp;
            }
        }
    }
}

int main(){
    int aa[6]={12,23,1,4,16,34};
    bubble_sort(aa,6);
    for(int i=0;i<6;i++)
        printf("%d,",aa[i]);
    printf("\n");
    return 0;
}