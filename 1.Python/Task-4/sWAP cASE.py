def swap_case(s):
    lis =[]
    for i in s:
        if i.isupper():
            lis.append(i.lower())
        elif i.islower():
            lis.append(i.upper())
        else:
            lis.append(i)  
    return ''.join(lis)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)