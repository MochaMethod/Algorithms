def countdown(i: int) -> None:
    """
    Takes integer i and uses recursion to count down.

    Args:
        i (int): A standard integer to count down from.

    Returns:
        None
    """
    print(i)
    if i <= 0:
        return

    else:
        countdown(i-1)

countdown(5)

def factorial(x: int) -> int:
    """
    Takes integer x and uses recursion to return the factorial value.

    Args:
        x (int): A standard integer type for the factorial.

    Returns:
        int: The factorial of x.
    """
    if x == 1:
        return 1

    else:
        return x * factorial(x - 1)