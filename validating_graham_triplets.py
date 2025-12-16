# Graham's 18 triples (p_k, m_k, r_k)
triples = [
    (3, 4, 1),
    (2, 3, 2),
    (5, 5, 1),
    (7, 8, 3),
    (17, 9, 4),
    (11, 10, 2),
    (47, 16, 7),
    (19, 18, 10),
    (61, 15, 3),
    (2207, 32, 15),
    (53, 27, 16),
    (31, 30, 24),
    (1087, 64, 31),
    (109, 27, 7),
    (41, 20, 10),
    (4481, 64, 63),
    (5779, 54, 52),
    (2521, 60, 60)
]

# Step 1: Collect all moduli m_k
moduli = [m for (_, m, _) in triples]

# Step 2: Compute LCM of all moduli (period of the covering)
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

L = 1
for m in moduli:
    L = lcm(L, m)

print("LCM of moduli =", L)

# Step 3: Check coverage over one full cycle [0, L)
covered = [False] * L

for (_, m, r) in triples:
    for n in range(r, L, m):
        covered[n % L] = True

# Step 4: Find uncovered integers (if any)
uncovered = [n for n in range(2, L) if not covered[n % L]]

if uncovered:
    print("Uncovered residues:", uncovered)
    print("Not a complete covering system!")
else:
    print("Every integer n ≥ 2 is covered by at least one congruence.")
