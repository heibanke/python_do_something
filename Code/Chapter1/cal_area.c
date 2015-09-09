/**********************
copyRight by heibanke
***********************/

#include <stdio.h>
#define ARRAY_LEN 4000

int main(){
    int array[ARRAY_LEN] = {0};
    int i,j,jinw,print_flag=0;
    array[ARRAY_LEN-1] = 1;
    //j代表次方数
    for(j=0; j<10000; j++){
        //i代表需要多少长度的数组更新，正确的长度是log10(x)
        jinw=0;
        for(i=ARRAY_LEN-1; i>=0; i--) {
            int tmp = array[i]*2+jinw;
            array[i] = tmp%10;
            jinw = tmp/10;
        }
    }
    //print the value
    for(j=0;j<ARRAY_LEN;j++){
        if(array[j]!=0 && print_flag==0)
            print_flag=1;
        
        if(print_flag==1)
            printf("%d",array[j]);
    }
    printf("\n");
    return 0;
}
