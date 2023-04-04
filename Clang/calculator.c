#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc <= 3 || argc > 4) {
        printf("\nInvalid args!\n\nProvide in this format : ./<file> <int> <int> <operator>\nWhere operator can be : Multiply, Divide, Sum or Subrtact\n\n");
        return 0;
    }

    char *operator = argv[3];
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    double total;

    if (strcmp(operator,"Sum") == 0) {
        total = a + b;
    }
    else if (strcmp(operator,"Multiply") == 0) {
        total = a * b;
    }
    else if (strcmp(operator,"Divide") == 0) {
        total = (double) a / b;
    }
    else if (strcmp(operator,"Subrtact") == 0) {
        total = a - b;
    }
    else {
        printf("\nGiven operator is not valid!\nShould be Multiply, Divide, Sum or Subrtact\n\n");
        return 0;
    }

    printf("%s of %s and %s is %f\n",operator,argv[1],argv[2],total);
    return 0;
}

int is_valid_operator(char **string) {
  return 0;
}
