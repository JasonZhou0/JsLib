#include "windows.h"

int main(void)
{
   system("@echo off");
   system("call Tools\\Python\\Python37-32\\python.exe Config\\BuildConfig\\Build.py");
   printf("\nThank you for your use! If you have any questions, please let me know.\n");
   for(int i=5;0<i;i--)
   {
      printf("\rThe window will close after %d seconds.",i);
      sleep(1);
   }
   return 0;
}