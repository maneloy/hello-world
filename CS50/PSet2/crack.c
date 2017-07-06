#define _XOPEN_SOURCE   //
#include <unistd.h>     // both required for using the 'crypt' function
#include <stdio.h>      // Compile with: cc -ggdb3 -O0 -std=c11 -Wall -Werror -Wshadow crack.c -lcrypt -lm -o crack
#include <string.h>     

int compare_strings(char *string1, char *string2);

/* can crack alphabetic passwords of up to 4 characters hashed with the function 'crypt' with salt 50 */
int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: ./crack hash\n");
        return 1;
    }

    char pass[5] = "";
    char i, j, k, l;
    int m;
    
    for (m = 0; m < 4; ++m) {
        for (i = 'A'; i <= 'z'; ++i) {
            pass[0] = i;
            if (compare_strings(argv[1], crypt(pass, "50")) == 1) {
                printf("%s\n", pass);
                return 0;
            }
            if (i == 'Z')
                i = '`';
            if (m >= 1) {
                for (j = 'A'; j <= 'z'; ++j) {
                    pass[1] = j;
                    if (compare_strings(argv[1], crypt(pass, "50")) == 1) {
                        printf("%s\n", pass);
                        return 0;
                    }
                    if (j == 'Z')
                        j = '`';
                    if (m >= 2) {
                        for (k = 'A'; k <= 'z'; ++k) {
                            pass[2] = k;
                            if (compare_strings(argv[1], crypt(pass, "50")) == 1) {
                                printf("%s\n", pass);
                                return 0;
                            }
                            if (k == 'Z')
                                k = '`';
                            if (m >= 3) {
                                for (l = 'A'; l <= 'z'; ++l) {
                                    pass[3] = l;
                                    if (compare_strings(argv[1], crypt(pass, "50")) == 1) {
                                        printf("%s\n", pass);
                                        return 0;
                                    }
                                    if (l == 'Z')
                                        l = '`';
                                }
                            }
                        }
                    }        
                }
            }
        }
    }
    return 0;
}

int compare_strings(char *string1, char *string2) {
    int i;
    int length;
    length = strlen(string1);
    
    for (i = 0; i < length; ++i)
        if (string1[i] != string2[i])
            return 0;
    return 1;
}

