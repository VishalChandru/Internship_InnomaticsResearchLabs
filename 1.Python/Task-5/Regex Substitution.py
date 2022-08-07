# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
   s = input()
   s = re.sub('\ \&{2}\ ',' and ',s)
   s = re.sub('\ \|{2}\ ',' or ',s)
   s = re.sub('\ \&{2}\ ',' and ',s)
   s = re.sub('\ \|{2}\ ',' or ',s)
   print(s)