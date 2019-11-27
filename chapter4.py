from math import floor

def euclidean(a: int, b: int):
    # a = b * q + r
    _q: int = int(floor(a / b))
    print(f"Quotient: {_q}")
    r: int = a % b
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