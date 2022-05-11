from secrets import randbelow
import sys
from pathlib import Path
from typing import Union


cdef long int _MAX_64_INT = 2**63 - 1
cdef int _MAX_32_INT = 2**31 - 1

# Make them visible to python code
MAX_64_INT = _MAX_64_INT
MAX_32_INT = _MAX_32_INT

cdef class Optimus:
    cdef public int max_int, prime, inverse, random

    def __init__(
        self, int prime, inverse: int = None, random: int = None, int bitlength = 64
    ):
        if bitlength not in (32, 64):
            raise ValueError("bitlength can only be 32 or 64")
        self.max_int = bitlength == 32 and _MAX_32_INT or _MAX_64_INT
        self.prime = prime
        if inverse is None:
            inverse = mod_inverse(prime, self.max_int)
        self.inverse = inverse
        if random is None:
            random = rand_n(self.max_int - 1)
        self.random = random

    cpdef int encode(self, int n):
        return ((n * self.prime) & self.max_int) ^ self.random

    cpdef int decode(self, int n):
        return ((n ^ self.random) * self.inverse) & self.max_int



cdef tuple egcd(int n, int p):
    if n == 0:
        return p, 0, 1
    else:
        g, y, x = egcd(p % n, n)
        return g, x - (p // n) * y, y

cpdef int mod_inverse(int n, int p):
    g, x, _ = egcd(n, p + 1)
    if g != 1:
        raise ValueError("modular inverse does not exist")
    else:
        return x % p

cpdef Optimus generate(
    str path_to_primes = "optimus-primes", int bitlength = 64
    # path_to_primes: Union[str, Path] = "optimus-primes", int bitlength = 64
):
    if bitlength not in (32, 64):
        raise ValueError("bitlength can only be 32 or 64")
    path_to_primes_ = Path(path_to_primes)

    if not (path_to_primes_.exists() and path_to_primes_.is_dir()):
        raise ValueError(f"{str(path_to_primes_)} does not exist or is not a directory")

    cdef int n = rand_n(50)
    cdef str input_file = str(path_to_primes_.joinpath(f"p{n}.txt").absolute())
    cdef int line_number = rand_n(1_000_000)

    with open(input_file, "r") as f:
        for _ in range(1, line_number):
            f.readline()
        return Optimus(int(f.readline().strip()), bitlength=bitlength)


cdef int rand_n(int n):
    return randbelow(n) + 1
