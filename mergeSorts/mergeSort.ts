const largeArrayToSort: number[] = [
  5, 18, 3, 10, 7, 12, 15, 2, 19, 4, 11, 6, 1, 9, 17, 8, 14, 20, 13, 16,
];
console.log("Array (TypeScript):", largeArrayToSort);

function merge(array: number[], left: number[], right: number[]): void {
  let i = 0;
  let j = 0;
  let k = 0;

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      array[k] = left[i];
      i++;
    } else {
      array[k] = right[j];
      j++;
    }
    k++;
  }

  while (i < left.length) {
    array[k] = left[i];
    i++;
    k++;
  }

  while (j < right.length) {
    array[k] = right[j];
    j++;
    k++;
  }
}

function mergeSort(array: number[]): void {
  if (array.length > 1) {
    const middle = Math.floor(array.length / 2);
    let left = array.slice(0, middle);
    let right = array.slice(middle);
    mergeSort(left);
    mergeSort(right);
    merge(array, left, right);
  }
}

mergeSort(largeArrayToSort);

console.log("After (TypeScript):", largeArrayToSort);
