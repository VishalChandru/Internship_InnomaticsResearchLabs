def merge_the_tools(string, k):
    # your code goes here
    for sub in zip(*[iter(string)] * k):
        dic = {}
        lis = [dic.setdefault(i, i) for i in sub if i not in dic]
        print(''.join(lis))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)