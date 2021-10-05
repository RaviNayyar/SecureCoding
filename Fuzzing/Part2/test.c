#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 128
#define FLAGSIZE 128

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
  fflush(stdout);
}

int main(int argc, char **argv){
  vuln();
  return 0;
}
