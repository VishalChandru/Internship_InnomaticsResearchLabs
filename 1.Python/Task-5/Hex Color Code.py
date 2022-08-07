# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    txt = input()
    s = txt.split()
    if len(s)>1 and  '{' not in s:
        s = re.findall(r'#[A-F0-9a-f]{3,6}',txt)
        if (s):
            [print(i) for i in s]