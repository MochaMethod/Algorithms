from typing import List, Any

def median(low: int, high: int) -> int:
    """
    Takes in two integer values and returns the median integer value.

    Args:
        low (int): The lower value of the two integers.
        high (int): The higher value of the two integers.

    Returns:
        int: The median integer of two values.
    """

    # Store all numbers between the low and high values
    num: List[int] = [] 
    if low >= high:
        return 0

    else:
        for i in range(high):
            num.append(i)

    # Check if number is odd or even
    if len(num) % 2 != 0:
        return round(num[int(len(num)/2)])
    
    else:
        return round(
            ((num[int((len(num)-1)/2)]) + (num[int(len(num)/2)]))/2
            )

m: int = median(1, 1023)
print(m)


def binarySearch(orderedList: List[Any], item: Any) -> int:
    """
    Takes in an ordered list and the item to find. 
    For example, find a specific name that starts with the letter K in a phone book.

    Args:
        orderedList (List): An ordered list that can contain any variable type.
        item (int): The item that you wish to find in the orderedList.

    Returns:
        int: The index where the item was found.

    """

    _low: int = 0
    _high: int = len(orderedList) - 1

    while _low <= _high:
        mid: int = _low + _high

        guess: Any = orderedList[mid]

        if guess == item:
            return mid

        if guess > item:
            _high = mid - 1

        elif guess <= item:
            _low = mid + 1

    return 0

orderedList: List[str] = ["Abby", "Abe", "Bryan", "Carl", "Ethan", "Frank", "John", "Kevin", "Nancy", "Oliver", "Phil"]
intOrderedList: List[int] = [1, 3, 5, 6, 8, 10, 23]

index: int = binarySearch(orderedList, "Kevin")
print("Guess: ", index, orderedList[index])
