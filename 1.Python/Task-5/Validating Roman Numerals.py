
thous = 'M{0,3}'
hunds = '(C[MD]|D?C{0,3})'
tens = '(X[CL]|L?X{0,3})'
ones = '(I[VX]|V?I{0,3})'

regex_pattern = r"%s%s%s%s$" % (thous, hunds, tens, ones)	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))