def fibonacci_add(bitsA, bitsB):
    """
    Adds two numbers given in Zeckendorf (Fibonacci) representation.
    bitsA, bitsB: lists of bits (LSB first), representing F2, F3, ...
    Returns: normalized Zeckendorf representation (LSB first)
    """

    # Stage 1: Naive bitwise sum
    n = max(len(bitsA), len(bitsB))
    S = [0] * (n + 3)  # extra space for carries

    for i in range(n):
        a = bitsA[i] if i < len(bitsA) else 0
        b = bitsB[i] if i < len(bitsB) else 0
        S[i] = a + b

    # Stage 2: Normalization loop
    changed = True
    while changed:
        changed = False

        # Rule 2: Eliminate 2s (2Fi → Fi+1 + Fi−2)
        for i in range(len(S)):
            if S[i] >= 2:
                carry = S[i] // 2
                S[i] %= 2
                S[i + 1] += carry          # carry left

                if i >= 2:
                    S[i - 2] += carry      # carry right by two
                else:
                    # Special cases: 2F2 = F3, or lower indices
                    S[i + 1] += carry

                changed = True

        # Rule 1: Eliminate adjacent 11s (Fi + Fi+1 → Fi+2)
        for i in range(len(S) - 2):
            if S[i] == 1 and S[i + 1] == 1:
                S[i] = 0
                S[i + 1] = 0
                S[i + 2] += 1              # carry left by two
                changed = True

    # Remove leading zeros
    while len(S) > 1 and S[-1] == 0:
        S.pop()

    return S
