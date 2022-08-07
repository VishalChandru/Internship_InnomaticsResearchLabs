# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean,std=map(float,input().split())
x=int(input())
y=int(input())

def normalDistribution(x, mean, std):
    return round(0.5 * 100 * (1 + math.erf((x - mean)/ (std * math.sqrt(2)))), 3)

print(round(100 - normalDistribution(x, mean, std), 2))
print(round(100 - normalDistribution(y, mean, std), 2))
print(round(normalDistribution(y,mean, std), 2))