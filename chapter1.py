def median(x: int, y: int) -> int:
    num: list = [] 

    if x >= y:
        return 0

    else:
        for i in range(y):
            num.append(i)

    if len(num) % 2 != 0:
        return round(num[int(len(num)/2)])
    
    else:
        return round(
            ((num[int((len(num)-1)/2)]) + (num[int(len(num)/2)]))/2
            )

m = median(1, 1000)
print(m)
    
