def factoral(x):
    if x == 0:
        return 1
    return x * factoral(x - 1)

x=int(input())
print(factoral(x))