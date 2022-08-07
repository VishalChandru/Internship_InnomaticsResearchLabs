import math
wgt,n,mean,sd=int(input()),int(input()),int(input()),int(input())
def centralLimitTheorem(wgt,n,mean,sd):
    newMean=n*mean
    newSd=(n**0.5)*sd     
    return round(0.5 * (1 + math.erf((wgt - newMean) / (newSd * (2 ** 0.5)))),4)

print(centralLimitTheorem(wgt,n,mean,sd))
