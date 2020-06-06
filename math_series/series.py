def fibonacci(n):
    """[The function returns the nth value in the fibonacci series]

    Args:
        n ([integer])
    Returns:
        [integer]: [nth value]
    """
    fibo = [0, 1]
    i = 1
           
    if n == 0:
        return 0
    else:
        while i <= n - 1:
            new = fibo[i - 1] + fibo[i]
            fibo.append(new)
            i += 1
        print(f"Fibonacci of {n} is {fibo[-1]}")
        return fibo[-1]


def lucas(n, a, b):
    """[This function returns the nth value in the lucas numbers]

    Args:
        n ([integer])
        a ([integer]): [1st value in lucas series]
        b ([integer]): [2nd value in lucas series]
    """
    lucas = [a, b]
    i = 1
    while i <= n -1:
        new = lucas[i - 1] + lucas[i]
        lucas.append(new)
        i += 1
    print(f"Lucas of {i} with {a} and {b} is {lucas[-1]}")
    return lucas[-1]

def sum_series(n, a=0, b=1):
    """[This functions determines which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.]

    Args:
        n ([integer]): [determines which element in the series to print]
        a ([integer]): [1st value in lucas series. If none, a = 0]
        b ([integer]): [2nd value in lucas series. If none, a = 1]
    """
    
    if type(n) != int or type(a) != int or type(b) != int or n < 0 or a < 0 or b <0:
        return 'Parameter(s) must be intergers >= 0'
    elif a != 0 or b != 1:
        return lucas(n, a, b)
    else:
        return fibonacci(n)

sum_series(3)
sum_series(8, 1, 3)
print(sum_series(6.3))