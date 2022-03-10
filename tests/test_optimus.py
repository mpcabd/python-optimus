import itertools
import pathlib
import secrets
import unittest

import optimus_id


class TestOptimus(unittest.TestCase):
    def test_mod_inverse(self):
        self.assertEqual(
            optimus_id.mod_inverse(309779747, optimus_id.MAX_32_INT), 49560203
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            optimus_id.Optimus(prime=5, bitlength=16)

        with self.assertRaises(ValueError):
            optimus_id.generate(bitlength=16)

        with self.assertRaises(ValueError):
            optimus_id.generate(path_to_primes="invalid-path")

    def test_generation(self):
        path = pathlib.Path("optimus-primes")
        if not (path.exists() and path.is_dir()):
            self.skipTest("optimus-primes not available for generation")

        o64 = optimus_id.generate()
        o32 = optimus_id.generate(bitlength=32)

        self.assertEqual(o64.decode(o64.encode(42)), 42)
        self.assertEqual(o32.decode(o32.encode(42)), 42)

    def test_encoding(self):
        optimus_instances = [
            optimus_id.Optimus(
                prime=309779747, inverse=49560203, random=57733611, bitlength=32
            ),
            optimus_id.Optimus(
                prime=684934207, inverse=1505143743, random=846034763, bitlength=32
            ),
            optimus_id.Optimus(
                prime=743534599, inverse=1356791223, random=1336232185, bitlength=32
            ),
            optimus_id.Optimus(
                prime=54661037, inverse=1342843941, random=576322863, bitlength=32
            ),
            optimus_id.Optimus(
                prime=198194831, inverse=229517423, random=459462336, bitlength=32
            ),
            optimus_id.Optimus(prime=198194831, random=459462336, bitlength=32),
        ]

        for i in range(5):
            o = optimus_instances[i]
            c = 10
            h = 100
            y = list(
                itertools.chain(
                    range(c),
                    (
                        secrets.randbelow(optimus_id.MAX_32_INT - 2 * c) + c
                        for _ in range(h)
                    ),
                    range(optimus_id.MAX_32_INT, optimus_id.MAX_32_INT - c - 1, -1),
                )
            )
            for n in y:
                encoded = o.encode(n)
                decoded = o.decode(encoded)
                with self.subTest(i=i, n=n):
                    self.assertEqual(decoded, n)


if __name__ == "__main__":
    unittest.main()
