def fibonacci(n):
    """Return the nth Fibonacci number with F0 = 0, F1 = 1."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def zeckendorf_decomposition(n):
    """
    Returns the list of Fibonacci indices used in the Zeckendorf
    representation of n (indices >= 2).
    """
    if n <= 0:
        return []

    # Generate Fibonacci numbers (F2 = 1, F3 = 2)
    fib = [1, 2]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])

    indices = []
    remaining = n
    i = len(fib) - 1

    while remaining > 0 and i >= 0:
        if fib[i] <= remaining:
            indices.append(i + 2)   # index shift: fib[0] = F2
            remaining -= fib[i]
            i -= 2                  # Zeckendorf rule
        else:
            i -= 1

    return indices


def egyption_division(knownFactor, product):
    """
    Computes the unknown factor n such that:
        knownFactor ◦ n = product
    using Egyptian (greedy) circular division.
    """

    if knownFactor == 0:
        raise ValueError("Division by zero")

    if product == 0:
        return 0

    # Step 1: Decompose knownFactor into Fibonacci indices
    indices = zeckendorf_decomposition(knownFactor)

    # Step 2: Generate basis table: V[k] = knownFactor ◦ F_k
    basisTable = {}
    k = 2

    while True:
        val = 0
        for idx in indices:
            val += fibonacci(idx + k)   # F_idx ◦ F_k = F_{idx+k}

        if val > product:
            break

        basisTable[k] = val
        maxK = k
        k += 1

    # Step 3: Greedy reconstruction of unknown factor
    unknownFactor = 0
    currentP = product

    k = maxK
    while k >= 2:
        termValue = basisTable.get(k, 0)

        if termValue <= currentP:
            currentP -= termValue
            unknownFactor += fibonacci(k)
            k -= 1    # skip next k (no consecutive 1s)

        if currentP == 0:
            break

        k -= 1

    return unknownFactor
