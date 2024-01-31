#include <stdio.h>
#include "sort.h"


int main(void)
{
    int numbers[] = {5, 2, 7, 4, 1, 6, 3, 0};
    int current = 7 ; // current is supposed to be equal size - 1 of the array
    int index = 0; // Moving pointer

    // while current > 0
    while (current > 0)
    {
    // Current value is greater than coming value array[index] > array[index + 1]
    if (numbers[index] > numbers[index + 1])
    {
        // Swap
        swap(&numbers[index], &numbers[index + 1]);
    }

    // index == end_of_array (current) - 1
    if (index == 7 - 1)
    {
        // decrement current
        current--;
        // reset index
        index = 0;
    }
    // else
    else
    {
        // increment index
        index++;
    }
    }

    print_array(numbers, 8);
    return (0);
}