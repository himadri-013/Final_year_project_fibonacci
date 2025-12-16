PROJECT OVERVIEW
----------------
This project studies arithmetic and structural properties of Fibonacci-based number systems from both algorithmic and number-theoretic perspectives. It demonstrates how integers represented using the Fibonacci (Zeckendorf) representation support well-defined addition, multiplication, and inverse operations, and how these ideas extend to the construction of Fibonacci-like sequences with strong divisibility guarantees.


PART I: ARITHMETIC IN THE FIBONACCI NUMBER SYSTEM
-------------------------------------------------
This part focuses on performing arithmetic directly in the Zeckendorf representation, where each integer is uniquely expressed as a sum of non-consecutive Fibonacci numbers.

Key contributions:
- Integer-to-Zeckendorf conversion using a greedy algorithm.
- A two-stage Fibonacci addition algorithm:
  * Naive bitwise summation aligned by Fibonacci place values.
  * Normalization using Fibonacci identities to eliminate invalid digits (2s) and adjacent 1s.
- Study and implementation of Knuth’s circle multiplication using shifted Fibonacci indices.
- Analysis of algebraic properties including clean partial products, strict monotonicity,
  uniqueness, and the cancellation law.
- Implementation of inverse circle multiplication (Egyptian division) via greedy reconstruction.


PART II: FIBONACCI-LIKE COMPOSITE SEQUENCES (GRAHAM’S CONSTRUCTION)
------------------------------------------------------------------
This part revisits a classical result by R. L. Graham showing that a Fibonacci-like sequence can be constructed in which every term is composite, even when the initial terms are coprime.

Key contributions:
- Reconstruction of Graham’s construction using:
  * Pisano periods of Fibonacci numbers modulo primes.
  * Divisibility triples (p, m, r).
  * Finite covering systems of congruences.
- Use of Fibonacci identities to enforce divisibility of sequence terms by fixed primes.
- Application of the Chinese Remainder Theorem to compute initial values satisfying all
  congruences simultaneously.
- Computational verification that the covering system spans all indices n ≥ 2.
- Exact reproduction of Graham’s original initial values, validating the theory.


MATHEMATICAL AND ALGORITHMIC SCOPE
---------------------------------
- Fibonacci numbers and recurrence relations
- Zeckendorf’s Theorem and canonical representations
- Non-standard arithmetic systems
- Modular arithmetic and Pisano periodicity
- Covering systems and the Chinese Remainder Theorem
- Greedy algorithms and normalization techniques


OUTCOME
-------
The project shows that the Fibonacci number system forms a consistent and reversible arithmetic
framework and that its structural properties can be leveraged to construct sequences with strong
global divisibility constraints. It bridges algorithm design and classical number theory through both
formal reasoning and computational validation.

REPOSITORY STRUCTURE
-------------------
This repository is organized into three branches to clearly separate documentation and the two
major technical components of the project:

- main
  Contains the complete project report and the README file.
  This branch serves as the primary reference for the theory, explanations, and overall project
  description.

- Fibonacci_arithmetic
  Contains all source code related to arithmetic in the Fibonacci (Zeckendorf) number system.
  This includes:
  * Integer-to-Zeckendorf conversion
  * Fibonacci addition with normalization
  * Knuth’s circle multiplication
  * Inverse circle multiplication (Egyptian division)

- Graham's_Composite_Series
  Contains all source code related to Graham’s construction of Fibonacci-like sequences with no
  prime terms.
  This includes:
  * Verification of Graham’s covering system
  * Pisano period computations
  * Chinese Remainder Theorem implementation
  * Reconstruction and validation of Graham’s initial conditions

This branching structure is intended to keep the theoretical exposition, Fibonacci arithmetic
algorithms, and number-theoretic constructions cleanly separated while remaining logically
connected.

