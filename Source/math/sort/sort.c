#include "sort.h"

u8 Sort_HighAndLowBitsReverse_8bits(u8 data)
{
   for(u8 i=0; i<sizeof(u8); i++)
   {
      if((u8)data & 0x01)
      {
         data = ((u8)data >> 1) | 0x80;
      }
      else
      {
         data = ((u8)data >> 1) & 0x7F;
      }
   }
   return (u8)data;
}