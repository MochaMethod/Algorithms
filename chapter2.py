from typing import List, Any

def findSmallest(arr: List[int]) -> int:
    smallest: int = arr[0]
    smallestIndex: int = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    
    return smallestIndex

def selectionSort(arr: List[int]) -> List[int]:
    newArr: List[int] = []

    for _ in range(len(arr)):
        smallest: int = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr

print(selectionSort([5, 3, 6, 2, 10, 85, 1, 49, 31]))