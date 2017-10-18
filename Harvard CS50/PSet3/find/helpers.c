/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include "cs50.h"
#include <stdio.h>
#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n) {
    // binary search
    int left, middle, right;
    left = 0;
    right = n - 1;
    middle = (left + right) / 2;
    while ((right - left) >= 0) { 
        if (value == values[middle])
            return true;
        else if (value < values[middle]) {
            right = middle - 1;
            middle = (left + right) / 2;
        }
        else if (value > values[middle]) {
            left = middle + 1;
            middle = (left + right) / 2;
        }
    }
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // counting sort
    int i, j;
    int counting_array[65536];
    for (i = 0; i < 65536; i++)
        counting_array[i] = 0;
    for (i = 0; i < n; i++)
        counting_array[values[i]]++;
    j = i = 0;
    while (j < n) {
        while (counting_array[i] > 0) {
            counting_array[i]--;
            values[j++] = i;
        }
        i++;
    }
    return;
}
