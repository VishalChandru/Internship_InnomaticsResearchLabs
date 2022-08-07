# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
x=list(map(float,input().split()))
y=list(map(float,input().split()))

def mean(x):
    return round(sum(x)/float(n),1)

def std(values,mean):
    data=[(val-mean)**2 for val in values]
    return (sum(data)/float(n))**0.5

def pearsonCorrelationCoefficient(x,y):
    a = sum( (x[i]-mean(x))*(y[i]-mean(y)) for i in range(int(n)))
    b = float(n)*std(x,mean(x))*std(y,mean(y))
    return round((a/b),3)

print(pearsonCorrelationCoefficient(x,y))