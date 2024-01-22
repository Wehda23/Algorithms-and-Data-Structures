#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef char* string;

typedef struct
{
    string name;
    string number;
} person;

void print(person individual);

#define PEOPLE_COUNT 2

bool name_exists(person *people, string value);
bool number_exists(person *people, string value);
bool exists(person *people, string value, string parameter);

int main(void)
{
    person people[PEOPLE_COUNT] = {
    {"Carter", "01123146469"},
    {"David", "01014938870"}
    };
    
    if (exists(people, "01014938870", "number"))
        return (0);

    printf("Not Found\n");
    return (1);
}

bool exists(person *people, string value,string parameter)
{
    bool exists = false;
    if (strcmp(parameter, "name") == 0)
        exists = name_exists(people, value);
    else if (strcmp(parameter, "number") == 0)
        exists = number_exists(people, value);

    return (exists);
}
bool name_exists(person *people, string value)
{
    for (int i = 0; i < PEOPLE_COUNT; i++)
    {
        if (strcmp(people[i].name, value) == 0)
        {
            printf("Found\n");
            return (true);
        }
    }
    return (false);
}
bool number_exists(person *people, string value)
{
    for (int i = 0; i < PEOPLE_COUNT; i++)
    {
        if (strcmp(people[i].number, value) == 0)
        {
            printf("Found\n");
            return (true);
        }
    }
    return (false);
}

void print(person individual)
{
    printf("Name: %s\nPhone: %s\n", individual.name, individual.number);
}

