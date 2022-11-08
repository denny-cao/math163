import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


a = "x^{2}"
b = "\\frac{1}{x}"

def clean(s):
    return s.replace("'", "").replace("\\\\", "\\")

def binomExpand(a, b, n):
    biex = ""
    biex2 = ""
    
    for k in range(n+1):
        biex += f"\\binom{ {n} }{ {k} } \\paren*{ {a} }^{ {n-k} } \\paren*{ {b} }^{ {k} }"
        biex2 += f"{ncr(n,k)} \\paren*{ {a} }^{ {n-k} } \\paren*{ {b} }^{ {k} }"
        if k + 1 != n + 1: 
            biex += " + "
            biex2 += " + "

    biex = clean(biex)
    biex2 = clean(biex2)
    
    print(biex + "\n\n" + biex2)

binomExpand(a, b, 12)