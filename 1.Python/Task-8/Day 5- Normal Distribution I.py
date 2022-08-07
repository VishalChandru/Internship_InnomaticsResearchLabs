# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean,std=map(float,input().split())
x=float(input())
y1,y2=map(float,input().split())

def normalDistribution(x,mean,std):
    return round(0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5)))),3)

print(normalDistribution(x,mean,std))
print(normalDistribution(y2,mean,std)-normalDistribution(y1,mean,std))