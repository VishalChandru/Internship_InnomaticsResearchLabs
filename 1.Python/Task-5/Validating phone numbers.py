# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    no = input()
    if re.match('(^[789]\d{9}$)',no):
        print('YES')
    else:
        print('NO')