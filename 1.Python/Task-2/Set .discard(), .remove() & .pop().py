n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command, *lis = input().split()
    lis = list(map(int,lis))
    if command == 'remove':
        s.remove(lis[0])
    if command == 'discard':
        s.discard(lis[0])
    if command == 'pop':
        s.pop()
print(sum(s))