# problem description: https://www.hackerrank.com/contests/pythonist/challenges/regex-2-validate-a-roman-number

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# need the '^' and '$' to specific the whole string match
pattern = re.compile('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
if pattern.match(raw_input()):
    print 'True'
else:
    print 'False'
