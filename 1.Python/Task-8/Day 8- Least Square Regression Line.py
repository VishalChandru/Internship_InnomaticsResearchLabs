# Enter your code here. Read input from STDIN. Print output to STDOUT
maths, stats = [],[]

for i in range(5):
    temp = list(map(int,input().split()))
    maths.append(temp[0])
    stats.append(temp[1])

def coeff_value(x,y):
    n = len(x)
    xy =[x[i]*y[i] for i in range(n)]
    x_square = [i**2 for i in x]
    
    coeff = (n*(sum(xy))-((sum(x)*sum(y))))/float(((n*sum(x_square))-sum(x)**2))
    return coeff
    
def linear_reg(x,y,pred_val):
    x_mean = sum(x)/float(len(x))    
    y_mean = sum(y)/float(len(y))
    coeff = coeff_value(x,y)
    const = y_mean - coeff*x_mean
    return (const + (coeff*pred_val))
    
predict = linear_reg(maths,stats,80)
print(predict)