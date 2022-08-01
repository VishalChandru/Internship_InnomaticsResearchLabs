# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = list(map(int,input().split()))
for i in range(1,n,2):
    print(('.|.'*i).center(m,'-'))
    
print('WELCOME'.center(m,'-'))

for j in range(n-2,0,-2):
    print(('.|.'*j).center(m,'-'))