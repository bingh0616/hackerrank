# problem description: https://www.hackerrank.com/contests/projecteuler/challenges/euler003

# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
def is_prime(n):
    print 'n', n
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True
'''

def prime_factors(n):
    pfs = []
    d = 2
    while n > 1:
        while n % d == 0:
            pfs.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1: pfs.append(n)
            break

    return pfs


n = input()
for i in xrange(n):
    num = input()
    print max(prime_factors(num))
