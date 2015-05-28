# problem description: https://www.hackerrank.com/contests/pythonist/challenges/python-time-delta
# python3 code, because python2 does not support %z

from datetime import datetime

for i in range(int(input())):
    dt1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(abs(int((dt1-dt2).total_seconds())))
