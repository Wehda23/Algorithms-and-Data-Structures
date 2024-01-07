import math

large_array_to_sort = [5, 18, 3, 10, 7, 12, 15, 2, 19, 4, 11, 6, 1, 9, 17, 8, 14, 20, 13, 16]
print("Array (Python):", large_array_to_sort)


def merge(array: list[int], left: list[int], right: list[int]) -> None:
    """
    Function used to merges and sorts two arrays

    Args:
        - array (list[int]): The original array that is being divided into two parts.
        - left: is a python datastructure <list> that contains only integer values
        - right: is a python datastructure <list> that contains only integer values
    
    Returns:
        Nothing.
    """
    # Create pointers
    left_index: int = 0
    right_index: int = 0
    main_index: int = 0
    """
    While loop continues until all elements from both lists are processed.
    It compares the current element of each list and appends the smaller one into `sorted_
    arr`. Then it moves on to the next element in this list. If any of these lists
    gets exhausted first then remaining elements will be added by the append statement.

    left: [1, 4, 5]  , right: [0, 2, 3]
           ^                   ^
    """
    while (left_index < len(left) and right_index < len(right)):
        # Check if left array is smaller than right array element
        if (left[left_index] > right[right_index]):
            array[main_index] = right[right_index]
            right_index += 1
        elif (left[left_index] <= right[right_index]):
            array[main_index] = left[left_index]
            left_index += 1
         
        # Increment main index
        main_index += 1
    
    while left_index < len(left):
        array[main_index] = left[left_index]
        left_index+=1
        main_index += 1
    
    while right_index < len(right):
        array[main_index] = right[right_index]
        right_index +=1
        main_index += 1


def mergeSort(array: list[int]) -> None:
    """
    Function used The Split an array

    Args:
        - Array: A python list datastructure that only contains integers.
    
    Returns:
        - Nothing.
    """
    # Base Case
    if len(array) > 1:
        # Declare a middle point, Left and Right
        middle: int = len(array) // 2
        left: list[int] = array[:middle]
        right: list[int] = array[middle:]

        # Split the array
        mergeSort(left)
        mergeSort(right)

        # Merge
        merge(array, left, right)


    

mergeSort(large_array_to_sort)
# Printing the sorted array
print(large_array_to_sort)
