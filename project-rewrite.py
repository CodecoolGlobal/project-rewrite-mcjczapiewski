def min(x, y):
    try:
        int(x), int(y)
        if x < y:
            return x
        else:
            return y
    except ValueError:
        print("At least one of given arguments is not a number!")


def max(x, y):
    try:
        int(x), int(y)
        if x > y:
            return x
        else:
            return y
    except ValueError:
        print("At least one of given arguments is not a number!")


def len(iterable):
    x = 0
    for i in str(iterable):
        x += 1
    return x


def multiply(x, y):
    try:
        if not int(x) == x or not int(y) == y:
            print("At least one of given numbers is not integer. Change it!")
        else:
            i = 1
            n = 0
            while i <= x:
                n = n + y
                i += 1
            return n
    except ValueError:
        print("At least one of given arguments is not a number!")


def pow(x, y):
    try:
        int(x), int(y)
        if not int(y) == y or not y > 0:
            print("Second argument must be a positive integer.")
        else:
            n = x
            i = 1
            while i < y:
                n = n * x
                i += 1
            return n
    except ValueError:
        print("At least one of given arguments is not a number!")


def divmod(x, y):
    try:
        int(x), int(y)
        if not int(x) == x or not int(y) == y:
            print("At least one of given numbers is not integer. Change it!")
        else:
            n = int(x / y)
            if n < 0:
                n = n - 1
            if (x < 0 and y > 0) or (x > 0 and y < 0):
                if x < 0:
                    while x < 0:
                        x = x + y
                elif y < 0:
                    while x > 0:
                        x = x + y
            elif x > 0 and y > 0:
                while x > y:
                    x = x - y
            elif x < 0 and y < 0:
                while x < y:
                    x = x - y
            values = (n, x)
            return values
    except ValueError:
        print("At least one of given arguments is not a number!")


print(min(5, 15))
print(max(5, 15))
print(len(48590))
print(multiply('a', 15))
print(pow(5, 3))
print(divmod(86, -7))
