/*************************************************
 * K&R, The C Programming Language: Sandbox/Test *
 *************************************************/

#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define abs(x) ((x) < 0 ? -(x) : (x))

int binsearch(int x, int v[], int n);
void prtarr(int arr[], int len);
void escape(char* s, char* t);
void unescape(char* s, char* t);
int atoii(char s[]);
void shellsort(int v[], int n);
void reverse(char s[]);
void expand(char s1[], char s2[]);
void itoa(int n, char s[], int padding);
void itob(int n, char s[], int b);
int trim(char s[]);
void count(void);

/* sandbox */
int main(void)
{
        int valores[] = {6,3,5,1,0,2,4,9,11,7,8,10};
        char s[] = "jaisfiajssiofja aj a   \n \n \t \t    ";
        trim(s);
        printf("%s\n", s);
        return 0;       
}

/* binsearch: find x in v[0] <= v[1] <= ... <= v[n-1] */
int binsearch(int x, int v[], int n)
{
        int low, high, mid;
        low = 0;
        high = n - 1;
        while (low <= high) {
                mid = (low + high) / 2;
                if (x < v[mid])
                        high = mid - 1;
                else if (x > v[mid])
                        low = mid + 1;
                else    /* found match  */
                        return mid;
        }
        return -1;      /* no match     */
}

/* prtarr: prints an integer array */
void prtarr(int arr[], int len)
{
        printf("[ ");
        for (int i = 0; i < len; i++)
                printf("%d ", arr[i]);
        printf("]\n");
}

/* escape: writes the string 's' in 't', replacing all special
           characters with their respective escape sequences */
void escape(char* s, char* t)
{
        int i = 0;
        int j = 0;
        char c;
        while ((c = s[i++]) != '\0') {
                switch (c) {
                case '\t':
                        t[j++] = '\\';
                        t[j++] = 't';
                        break;
                case '\n':
                        t[j++] = '\\';
                        t[j++] = 'n';
                        break;
                default:
                        t[j++] = c;
                }
        }
        t[j] = '\0';
}

/* unescape: writes the string 's' in 't', replacing all escape
             sequences with their respective special characters */
void unescape(char* s, char* t)
{
        int i = 0;
        int j = 0;
        char c;
        while ((c = s[i] != '\0')) {
                if (s[i] != '\\')
                        t[j++] = s[i];
                else
                        switch (s[++i]) {
                        case 'n':
                                t[j++] = '\n';
                                break;
                        case 't':
                                t[j++] = '\t';
                                break;
                        default:
                                t[j++] = '\\';
                                t[j++] = s[i];
                                break;
                        }
        i++;
        }
        t[j] = '\0';
}

/* atoi: convert s to integer; version 2 */
int atoii(char s[])
{
        int i, n, sign;
        
        for (i = 0; isspace(s[i]); i++) /* skip white space */
                ;
        sign = (s[i] == '-') ? -1 : 1;
        if (s[i] == '+' || s[i] == '-')     /* skip sign */
                i++;
        for (n = 0; isdigit(s[i]); i++)
                n = 10 * n + (s[i] - '0');
        return sign * n;
}

/* shellsort: sort v[0]...v[n-1] into increasing order */
void shellsort(int v[], int n)
{
        int gap, i, j, temp;
        
        for (gap = n / 2; gap > 0; gap /= 2)
                for (i = gap; i < n; i++)
                        for (j=i-gap; j >= 0 && v[j]>v[j+gap]; j-=gap) {
                                temp = v[j];
                                v[j] = v[j+gap];
                                v[j+gap] = temp;
                        }
}

/* reverse: reverse string s in place */
void reverse(char s[])
{
        int c, i, j;
        
        for (i = 0, j = strlen(s)-1; i < j; i++, j--) {
                c = s[i];
                s[i] = s[j];
                s[j] = c;
        }
}

/* expand: expand shorthand notation in s1 into string s2 */
void expand(char s1[], char s2[])
{
        char c;
        int i, j;
        
        i = j = 0;
        while ((c = s1[i++]) != '\0')     /* fetch a char from s1[] */
                if (s1[i] == '-' && s1[i+1] >= c) {
                        i++;
                        while (c < s1[i]) /* expand shorthand */
                                s2[j++] = c++;
                } else {
                        s2[j++] = c;      /* copy the character */
                }
        s2[j] = '\0';
}

/* itoa: convert n to characters in s padded to a certain minimum field */
void itoa(int n, char s[], int padding)
{
        int i = 0;
        int sign = n;
        int count = 0;
        
        do {                                      /* generate digits in reverse order */
                s[i++] = (abs (n % 10)) + '0';  /* get next digit */
                count++;
        } while ((n /= 10) != 0);                 /* delete it */
        if (sign < 0)
                s[i++] = '-';
        while (count++ < padding)
                s[i++] = ' ';
        s[i] = '\0';
        reverse(s);
}

/* itob: convert n to characters in s - base b */
void itob(int n, char s[], int b)
{
        int i, j, sign;
        if ((sign = n) < 0)
                n = -n;
        i = 0;
        do {                                      /* generate digits in reverse order */
                j = n % b;                        /* get next digit */
                s[i++] = (j <= 9) ? j+'0' : j+'a'-10;
        } while ((n /= b) > 0);                   /* delete it */
        if (sign < 0)
                s[i++] = '-';
        s[i] = '\0';
        reverse(s);
}

/* trim: remove trailing blank, tabs, newlines */
int trim(char s[])
{
        int n;
        
        for (n = strlen(s) - 1; n >= 0; n--)
                if (s[n] != ' ' && s[n] != '\t' && s[n] != '\n')
                        break;
        s[n+1] = '\0';
        return n;
}

void count(void)
{
        int c, nwhite, nother, ndigit[10];
        
        nwhite = nother = 0;
        for (int i = 0; i < 10; i++)
                ndigit[i] = 0;
        
        while ((c = getchar()) != EOF) {
                switch(c) {
                case '0': case '1': case '2': case '3': case '4':
                case '5': case '6': case '7': case '8': case '9':
                        ndigit[c-'0']++;
                       break;
                case ' ':
                case '\n':
                case '\t':
                        nwhite++;
                        break;
                default:
                        nother++;
                        break;
                }
        }
        printf("digits =");
        for (int i = 0; i < 10; i++)
                printf(" %d", ndigit[i]);
        printf(", white space = %d, other = %d\n", nwhite, nother);
}
