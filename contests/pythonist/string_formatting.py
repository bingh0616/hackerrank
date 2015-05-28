# problem description: https://www.hackerrank.com/contests/pythonist/challenges/python-string-formatting

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
width = len('{:b}'.format(n))

for i in xrange(1, n+1):
    print '{0:{1}} {0:{1}o} {0:{1}X} {0:{1}b}'.format(i, width)

