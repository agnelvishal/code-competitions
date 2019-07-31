#include <stdio.h>
int main() {
  int i, b, t, c[10];
  i=0;

  //below code from https://stackoverflow.com/questions/9599794/putting-numbers-separated-by-a-space-into-an-array
  while (i<4 && scanf("%d", &c[i++]));

 for (i=0;i<4;i++)
  printf("%d ",c[i]);
  
  return 0;
}

