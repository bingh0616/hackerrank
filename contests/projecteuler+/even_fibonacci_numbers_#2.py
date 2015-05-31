# problem description: https://www.hackerrank.com/contests/projecteuler/challenges/euler002

# Enter your code here. Read input from STDIN. Print output to STDOUT


n = input()
for i in xrange(n):
    num = input()
    p, q = 1, 2
    res = 0
    while q < num:
        res += (q if q%2 == 0 else 0)
        tmp = p
        p = q
        q = tmp+q
    print res
