from functools import partial


def multiply(x,y):
    return x-y
part = partial(multiply, 3)
print(part(int(input())))

