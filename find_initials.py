# Fibonacci mod calculation
def fib_mod(n, mod):
    a, b = 0, 1
    for _ in range(n):
        a, b = b % mod, (a + b) % mod
    return a


# Graham's 18 triples (p, m, r)
triples = [
    (3, 4, 1), (2, 3, 2), (5, 5, 1), (7, 8, 3), (17, 9, 4), (11, 10, 2),
    (47, 16, 7), (19, 18, 10), (61, 15, 3), (2207, 32, 15), (53, 27, 16),
    (31, 30, 24), (1087, 64, 31), (109, 27, 7), (41, 20, 10),
    (4481, 64, 63), (5779, 54, 52), (2521, 60, 60)
]

# Step 1: Compute congruences for A0 and A1
a0_congruences = []
a1_congruences = []

for (p, m, r) in triples:
    a0 = fib_mod(m - r, p)
    a1 = fib_mod(m - r + 1, p)
    a0_congruences.append((a0, p))
    a1_congruences.append((a1, p))


# Step 2: Chinese Remainder Theorem solver
def crt(congruences):
    x, M = 0, 1
    for (_, mod) in congruences:
        M *= mod

    for (a, mod) in congruences:
        Mi = M // mod
        inv = pow(Mi, -1, mod)   # modular inverse
        x = (x + a * Mi * inv) % M

    return x, M


# Step 3: Compute A0 and A1
A0, mod_A0 = crt(a0_congruences)
A1, mod_A1 = crt(a1_congruences)

print("A0 =", A0)
print("A1 =", A1)

'''
output :

A0 = 331635635998274737472200656430763
A1 = 1510028911088401971189590305498785

'''