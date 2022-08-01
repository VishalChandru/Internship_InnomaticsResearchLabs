# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = set(map(int,input().split()))
m = int(input())
brr = set(map(int,input().split()))
print(len(arr.union(brr)))