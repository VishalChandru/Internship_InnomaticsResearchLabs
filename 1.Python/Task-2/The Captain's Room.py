# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
arr = list(map(int,input().split()))
uniq = set(arr)
room = ((sum(uniq)*k) - sum(arr))//(k-1)
print(room)