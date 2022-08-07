# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
cons = 'qwrtypsdfghjklzxcvbnm'
vol = 'aeiou'
x = re.findall(r'(?<=[%s])([%s]{2,})[%s]'%(cons,vol,cons),input(),flags=re.I)
print('\n'.join(x or ['-1']))