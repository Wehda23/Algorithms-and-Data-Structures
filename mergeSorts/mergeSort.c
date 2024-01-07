#include <stdio.h>

void printArray(int *array, const int size);
void merge(int *array, int start, int middle, int end);
void mergeSort(int *array, int start, int end);

void main(void){
    int largeArrayToSort[20] = {5, 18, 3, 10, 7, 12, 15, 2, 19, 4, 11, 6, 1, 9, 17, 8, 14, 20, 13, 16};
    int size = sizeof(largeArrayToSort)/sizeof(largeArrayToSort[0]);

    mergeSort(largeArrayToSort, 0, 19);
    printArray(largeArrayToSort, sizeof(largeArrayToSort)/sizeof(largeArrayToSort[0]));

}


void merge(int *array, int start, int middle, int end)
{   
    /* Get the sizes of subarrays */
    int leftSize = middle - start + 1;
    int rightSize = end - middle;
    /* initiate subarrays with correct sizes */
    int L[leftSize], R[rightSize];

    /* Fill them in */
    for (int i = 0; i < leftSize; i++)
        L[i] = array[start + i];
    
    for (int j = 0; j < rightSize; j++)
        R[j] = array[middle + 1 + j];
    
    /* Create the indexing pointers of each array */
    /* 
    Practically i, is for newly created array
    j is for newly created right array
    k is for the parent/main array to indicate where you at from there
    [1, 2, 3, 17, 29, 18, 4]
               ^
               k
    Where the change is going to occure at the main array
    */
    int i, j, k;
    i = 0;
    j = 0;
    k = start;

    while (i < leftSize && j < rightSize) {
    if (L[i] <= R[j]) {
      array[k] = L[i];
      i++;
    } else {
      array[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < leftSize) {
    array[k] = L[i];
    i++;
    k++;
  }

  while (j < rightSize) {
    array[k] = R[j];
    j++;
    k++;
  }
}

void mergeSort(int *array, int start, int end)
{
    /* Base case should be when the start is larger than or equal to end*/
    if (start < end)
    {
    /* We will get the middle point */
    int middle = start + (end - start) / 2;
    mergeSort(array, start, middle);
    mergeSort(array, middle + 1, end);

    merge(array, start, middle, end);
    }
}

void printArray(int *array, const int size)
{
    printf("\nArray (C): ");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}


