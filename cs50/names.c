#include <stdio.h>
#include <string.h>

typedef char* string;

int main(void)
{

    string names[] = {"Waheed", "Khaled", "Mohamed", "Elhariri"};

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(names[i], "Khaled") == 0)
        {
            printf("Found\n");
            return (0);
        }
    }

    printf("Not Found\n");
    return (1);
}