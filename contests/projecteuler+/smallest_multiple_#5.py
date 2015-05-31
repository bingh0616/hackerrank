# problem description: https://www.hackerrank.com/contests/projecteuler/challenges/euler005

# Enter your code here. Read input from STDIN. Print output to STDOUT
def gcd(a, b):
    if a > b: b, a = a, b
    if a == 0: return b
    return gcd(b%a, a)

def lcm(a, b):
    return (a*b) / gcd(a,b)

n = input()
for i in xrange(n):
    num = input()
    vals = range(1, num+1)
    print reduce(lcm, vals)
