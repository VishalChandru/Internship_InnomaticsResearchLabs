# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int,input().split()))
m = int(input())
for i in range(m):
    command, size = input().split()
    size = int(size)
    arr = set(map(int,input().split()))
    if command == 'intersection_update':
        A.intersection_update(arr)
    if command == 'update':
        A.update(arr)
    if command == 'symmetric_difference_update':
        A.symmetric_difference_update(arr)
    if command == 'difference_update':
        A.difference_update(arr)
print(sum(A))