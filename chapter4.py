from math import floor
from typing import List

def euclidean(a: int, b: int):
    """
    Uses the Euclidean algorithm to determine the GCD of two itegers.

    Args:
        a (int): Integer a can be a negative or positive value.
        b (int): Integer b must follow 0 <= r < b

    Returns:
        int: The GCD of a and b.
    """
    
    # a = b * q + r
    _q: int = int(floor(a / b))
    print(f"Quotient: {_q}")
    r: int = a % b

    # 0 <= r < b
    if 0 > r:
        print(f"0 is greater than remainder {r}.")
        return 0

    if r > b:
        print(f"Remainder {r} is greater than integer {b}")
        return 0

    print(f"Remainder: {r}")
    a = b
    print(f"A = B({a})")
    b = r
    print(f"B = R({b})")

    # a = 0; gcd(0, b) = b
    if a == 0:
        print(f"Returning value a({b}) | type: {type(b)}")
        return b
    
    # b = 0; gcd(a, 0) = a 
    elif b == 0:
        print(f"Returning value a({a}) | type: {type(a)}")
        return a

    else:
        return euclidean(a, b)

a: int = 270
b: int = 192
gcd: int = euclidean(a, b)
print(f"GCD type: {type(gcd)}")
print(f"GCD({a}, {b}) = {gcd}")


def sum(arr: List[int], total: int=0):
    """
    A recursive function to find the sum of all integers in an array.

    Args:
        arr (List): An array of integers.
        total (int): The total sum of integers in a list (defaults to 0).

    Returns:
        int: The total sum of integers in a list.
    """

    if len(arr) <= 0:
        return total

    else:
        # Increment total by first index in array.
        total += arr[0]
        # Remove first index in array to avoid adding the same number twice.
        arr.pop(0)
        
        return sum(arr, total)

total: int = sum([1, 2, 3, 4, 5, 7, 9, 15])
print(f"Total sum of ints in list: {total}")