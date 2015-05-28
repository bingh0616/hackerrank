# problem description: https://www.hackerrank.com/contests/pythonist/challenges/python-sort-sort

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, raw_input().split())

ls = []
for i in range(n):
    ls.append(map(int, raw_input().split()))
    
k = input()
ls = sorted(ls, key=lambda a:a[k])

for l in ls:
    print ' '.join(map(str, l))


