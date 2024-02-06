def factorial(n):
    sol = n if n != 0 else 1
    for i in range(1,n):
        sol *= (n - i)
    return sol