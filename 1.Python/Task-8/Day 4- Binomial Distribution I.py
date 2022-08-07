# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
    
p = 1.09/(1+1.09)
ans = 0
for i in range(3,7):
    ans += factorial(6) / factorial(i) / factorial(6-i) * p**i * (1-p)**(6-i)
print(round(ans, 3))