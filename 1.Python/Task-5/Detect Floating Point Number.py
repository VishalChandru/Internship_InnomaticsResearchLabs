# Enter your code here. Read input from STDIN. Print output to STDOUTt
import re
n = int(input())
for i in range(n):
    if re.match('[+-.]?\d*\.\d+$',input()) != None:
        print(True)
    else:
        print(False)