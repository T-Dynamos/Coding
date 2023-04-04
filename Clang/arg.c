#include <stdio.h>

int main(int argc, char **argv){
    printf("Total args : %d | File name : %s\n\n",argc-1,argv[0]);
    int loop_;
    for (loop_ = 0;loop_ <= argc-2;loop_++) {
      printf("%d: %s\n",(loop_+1),argv[loop_+1]);
  }
}
