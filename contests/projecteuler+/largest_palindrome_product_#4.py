# problem description: https://www.hackerrank.com/contests/projecteuler/challenges/euler004

# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_palinum(n):
    div = 1
    while n>10*div:
        div *= 10
    while n>0 and n/div == n%10:
        n %= div
        n /= 10
        div /= 100
    return n == 0

n = input()
for i in xrange(n):
    num = input()
    max_v = 101101
    for m in xrange(999, 99, -1):
        for n in xrange(m, 99, -1):
            if m*n < num and m*n > max_v and is_palinum(m * n):
                max_v = m * n
                break
    print max_v
                


