# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
c = complex(input())
print(round(abs(c),3))
print(round(cmath.phase(c),3))
