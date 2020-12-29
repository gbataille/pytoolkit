import gmpy2
from factordb.factordb import FactorDB
from gmpy2 import mpz


def decrypt(e, c, n) -> mpz:
    f = FactorDB(n)
    f.connect()
    p, q = f.get_factor_list()

    phi = gmpy2.mul(p - 1, q - 1)
    d = gmpy2.invert(e, phi)
    return gmpy2.powmod(c, d, n)
