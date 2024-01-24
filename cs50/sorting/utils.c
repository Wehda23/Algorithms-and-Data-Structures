#include <stdio.h>
#include "sort.h"



/**
 * @brief print_array - Function that is used to print an array of integers
 * @param array: array that is going to be printed.
 * @param size: Represents the size of input array.
 */
void print_array(int *array, int size)
{
    printf("{");
    for (int i = 0; i < size; i++)
    {
        printf("%d", array[i]);
        if (i != size - 1)
            printf(", ");
    }
    printf("}\n");
}


/**
 * @brief swap - Function that swaps two integer values
 * @param first: Represents the first integer pointer
 * @param second: Represents the second integer pointer
 */
void swap(int *first, int *second)
{
    int temp = *first;
    *first = *second;
    *second = temp;
}