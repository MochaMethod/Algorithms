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

print(selectionSort([5, 3, 6, 2, 10, 85, 1, 49, 31]from typing import List, Any

def findSmallest(arr: List[int]) -> int:
    """
    Takes in a list full of integers in any order, and finds the smallest number in the list.

    Args:
        arr (List): An ordered list that can contain integer types. Does not need to be ordered.

    Returns:
        int: The smallest integer in the list.

    """
    
    smallest: int = arr[0]
    smallestIndex: int = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    
    return smallestIndex

def selectionSort(arr: List[int]) -> List[int]:
    """
    Takes in a list full of integers in any order, and returns an ordered list of integers.

    Args:
        arr (List): An ordered list that can contain integer types. Does not need to be ordered.

    Returns:
        int: An ordered list of integers.
    """

    newArr: List[int] = []

    for _ in range(len(arr)):
        smallest: int = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr

print(selectionSort([5, 3, 6, 2, 10, 85, 1, 49, 31]))))
