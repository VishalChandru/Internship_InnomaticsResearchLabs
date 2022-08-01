# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    n = int(input())
    arr = set(map(int,input().split()))
    m = int(input())
    brr = set(map(int,input().split()))
    if arr.intersection(brr) == arr:
        print(True)
    else:
        print(False)