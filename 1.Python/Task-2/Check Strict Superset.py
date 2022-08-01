# Enter your code here. Read input from STDIN. Print output to STDOUT
arr = set(map(int,input().split()))
n = int(input())
lis =[]
for i in range(n):
    a = set(map(int,input().split()))
    if arr.intersection(a)==a and len(arr)!=len(a):
        lis.append(True)
    else:
        lis.append(False)
res = True
for i in lis:
    res = res and i
print(res)