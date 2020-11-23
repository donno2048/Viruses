#include <string.h>
void func(char *str){
  char buffer[16];
  strcpy(buffer, str);}
void main(){
  char large[2 ** 100];
  int i;
  for(i = 0; i < 2 ** 100; i++)
    large[i] = '*';
  func(large);}
