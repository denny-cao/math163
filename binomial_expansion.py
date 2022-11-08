from math import comb

'''
Expands binomial in the form (ca^d + kb^e)^n in LaTeX
\DeclarePairedDelimiter\paren{(}{)}
'''

def binomial_theorem(c: float, a: str, d: int, k: float, b: str, e: int, n: int) -> str:
    for i in range(n + 1):
        pow1 = d * (n - i)
        pow2 = i
        coefficient = comb(n, i) * (c ** pow1) * (k ** pow2)
        term = ""
        if coefficient == 1:
            coefficient = ''
        if e < 0:
            term = f"{coefficient}\\paren{'*'}{{{a}{'^'}{{{pow1}}}}}" + f"\\paren{'*'}{{\\frac{{1}}{{{b}{'^'}{{{pow2}}}}}}}"
        else:
            term = f"{coefficient}\\paren{'*'}{{{a}{'^'}{{{pow1}}}}}" + f"\\paren{'*'}{{{b}{'^'}{{{pow2}}}}}"
        if coefficient == 0:
            term = ''
        first = ''
        if term[0] != '-' and i != 0:
            first = '+'
        print(first + term, end='')
    print()
if __name__ == '__main__':
    binomial_theorem(1, "x", 2, -1, "x", -1, 12)


