if __name__ == '__main__':
    N = int(input())
    a = []
    for i in range(N):
        command, *lis = input().split()
        lis = list(map(int,lis))
        if command == 'append':
            a.append(lis[0])
        elif command == 'insert':
            a.insert(lis[0],lis[1])
        elif command == 'remove':
            a.remove(lis[0])
        elif command == 'pop':
            a.pop()
        elif command == 'sort':
            a = sorted(a)
        elif command == 'reverse':
            a.reverse()
        elif command == 'print':
            print(a)