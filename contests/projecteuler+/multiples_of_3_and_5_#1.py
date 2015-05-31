# problem description: https://www.hackerrank.com/contests/projecteuler/challenges/euler001

# Enter your code here. Read input from STDIN. Print output to STDOUT

def sum(first, num):
    n = num/first
    last = n * first
    return (first+last)*n / 2
# res = sum(3) + sum(5) - sum(15)
n = input()
for i in xrange(n):
    num = input()
    print sum(3, num-1) + sum(5, num-1) - sum(15, num-1)
