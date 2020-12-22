[![Build Status](https://travis-ci.com/mpcabd/python-optimus.svg?branch=main)](https://travis-ci.com/mpcabd/python-optimus)

# python-optimus
This is based fully on [pjebs/optimus-go](https://github.com/pjebs/optimus-go) for Go which is based on [jenssegers/optimus](https://github.com/jenssegers/optimus) for PHP which is based on Knuth's Integer Hashing (Multiplicative Hashing) from his book [The Art Of Computer Programming, Vol. 3, 2nd Edition](https://archive.org/details/B-001-001-250/page/n535/mode/2up), Section 6.4, Page 516.

With this library, you can transform your internal id's to obfuscated integers based on Knuth's integer hash. It is similar to [Hashids](https://hashids.org/), but will generate integers instead of random strings. It is also super fast.

    >>> my_optimus.encode(42)
    7773166408443174426
    >>> my_optimus.decode(7773166408443174426)
    42

This library supports both 32 and 64 bits integers, although in Python you don't have that differentiation between int32 and int64, even bigint or bignum is the same since [PEP 237](https://www.python.org/dev/peps/pep-0237/). The reason you need a bitlength is that the algorithm itself works on a fixed bitlength. By default this library uses 64 bits.

## Python Support

So far it's only tested on Python 3.8 and Python 3.9

## Installation

    pip install python-optimus

## Usage

Basic usage:

```python
from optimus_ids import Optimus
my_optimus = Optimus(
    prime=<your prime number>
)
my_int_id = <some id you have>
my_int_id_hashed = my_optimus.encode(my_int_id)
assert my_int_id == my_optimus.decode(my_int_id_hashed)
```

The caveat with the usage above is that every time you create your `Optimus` instance it will have a random component, even with using the same prime, so a proper usage should be like this:

```python
from optimus_ids import Optimus
my_optimus = Optimus(
    prime=<your prime number>,
    random=<some random number>
)
my_int_id = <some id you have>
my_int_id_hashed = my_optimus.encode(my_int_id)
assert my_int_id == my_optimus.decode(my_int_id_hashed)

```

To generate a suitable random number you could do this:

```python
from optimus_ids import rand_n, MAX_64_INT  # use 32 instead of 64 if you want to
my_random_number = rand_n(MAX_64_INT - 1)
```

You can also generate an `Optimus` intance and then keep its `prime`, `inverse` and `random` properties stored, so you can always configure a new instance with the same components, or even pickle it:

```python
from optimus_ids import generate, Optimus
my_optimus = generate()

# store the following variables or pickle the my_optimus variable
prime = my_optimus.prime
inverse = my_optimus.inverse
random = my_optimus.random
bitlength = my_optimus.bitlength

# create a new instance with the same parameters or unpickle an instance
my_other_optimus = Optimus(
    prime=prime,
    inverse=inverse,
    random=random,
    bitlength=bitlength,
)
assert my_optimus.encode(42) == my_other_optimus.encode(42)
assert my_optimus.decode(my_other_optimus.encode(42)) == my_other_optimus.decode(my_optimus.encode(42))
```

**NOTE** for the generate function to work, it needs data, the data is large, and not available with the package, the data should be downloaded from [here](https://github.com/pjebs/optimus-go-primes) and the path to it is passed to the `generate` function. By default it expects the data to be in a folder called `optimus-primes` in the current working directory.

```
├── your-app.py
├── ...
└── optimus-primes
    ├── p1.txt
    ├── p2.txt
    ├── ...
    └── p50.txt
```

Check the [tests](tests/) folder for test cases and other usage examples.

## License

This work is licensed under
[MIT License](https://opensource.org/licenses/MIT).
