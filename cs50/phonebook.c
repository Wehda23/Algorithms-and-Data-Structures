#include <stdio.h>
#include <string.h>

typedef char* string;


int main(void)
{

    string names[] = {"Carter", "David"};
    string numbers[] = {"01123146469", "01014938870"};

    for (int i = 0; i < 2; i++)
    {
        if (strcmp(names[i], "David") == 0)
        {
            printf("Found Phone: %s\n", numbers[i]);
            return (0);
        }
    }

    return (1);
}