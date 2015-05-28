# problem description: https://www.hackerrank.com/contests/pythonist/challenges/regex-1-validating-the-phone-number

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# need the '^' and '$' to specific the whole string match
pattern = re.compile('^[7-9]\d{9}$')
for i in range(input()):
    if pattern.match(raw_input()):
        print 'YES'
    else:
        print 'NO'
