#include <stdio.h>
#include "types.h"
#include "sort.h"

int ret = 0x00;
int main( void )
{
   printf("%d\r\n",0x01);
   ret = Sort_HighAndLowBitsReverse_8bits(0x01);
   printf("%d\r\n",ret);
   while(1);
}