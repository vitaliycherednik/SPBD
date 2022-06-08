import math
from sympy import *

# Fast discrete potentiation
def fast_discrete_potentiation(message, key, parameter):
    binaryKey = bin(key).replace('0b', '')
    cypher = 1
    for i in range(len(binaryKey)):
        cypher = ((cypher ** 2) * (message ** int(binaryKey[i]))) % parameter
    return cypher

message = int(input('Input the message: '))
key = int(input('Input the public key: '))
parameter = int(input('Input P-parameter: '))

print('\nCipher E = ', fast_discrete_potentiation(message, key, parameter), '\n')


# Generate large prime numbers
def largePrimeNumber(p_max, simpleNumber):
    k = math.ceil(math.log(p_max / 2, simpleNumber))
    p1 = 2 * (simpleNumber ** k) + 1
    p2 = 2 * (simpleNumber ** k) - 1
    if fast_discrete_potentiation(2, p1 - 1, p1) == 1:
        p = p1
    if fast_discrete_potentiation(2, p2 - 1, p2) == 1:
        p = p2
    else:
        while fast_discrete_potentiation(2, p1 - 1, p1) != 1:
            p1 += 2
        p = p1
    return p

p_max = int(input('Input Pmax number: '))
primeSmallNumber = int(input('Input small prime number: '))

if isprime(primeSmallNumber):
    print('\nPrime number P was generated: ', largePrimeNumber(p_max, primeSmallNumber))
else:
    print("\nThe small number entered is not prime. Try another one.")
