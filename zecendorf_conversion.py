def integer_to_zeckendorf(n):
    """
    Converts a positive integer n to its Zeckendorf (Fibonacci) representation.
    Returns a bit string with MSB first.
    F2 = 1, F3 = 2, ...
    """

    if n <= 0:
        raise ValueError("n must be a positive integer")

    # Generate Fibonacci numbers up to n (F2 = 1, F3 = 2)
    fib = [1, 2]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])

    remaining = n
    used = [0] * len(fib)

    i = len(fib) - 1
    if fib[i] > remaining:
        i -= 1

    # Greedy selection process
    while remaining > 0 and i >= 0:
        if fib[i] <= remaining:
            used[i] = 1
            remaining -= fib[i]
            i -= 2          # skip next Fibonacci number
        else:
            i -= 1

    # Trim unused leading zeros
    while len(used) > 1 and used[-1] == 0:
        used.pop()

    # Return MSB-first bit string
    bit_string = ''.join(map(str, reversed(used)))
    return bit_string
