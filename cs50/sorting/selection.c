#include <stdio.h>
#include "sort.h"



int main(void)
{
    int numbers[] = {5, 2, 7, 4, 1, 6, 3, 0};
    int current = 0;
    int index = 0;
    int smallest = numbers[0], smallest_index = 0;
    int steps = 0;

    while (current < 8)
    {
        if (numbers[index] < smallest)
        {
            smallest = numbers[index];
            smallest_index = index;
        }
        // Reached the end of the array
        if (index == 7)
        {    
            // swap
            swap(&numbers[current], &numbers[smallest_index]);
            // Increment current
            current++;
            // restate index
            index = current;
            // Restate smallest_index and smallest value
            smallest_index = current;
            smallest = numbers[current];
        }
        else
            index++;
        
        steps++;
    }
    
    print_array(numbers, 8);

    printf("\nSteps: %d", steps);
    return (0);
}