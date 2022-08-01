import textwrap

def wrap(string, max_width):
    lis = []
    for i in range(0,len(string),max_width):
         lis.append(string[i:max_width+i]+'\n')
    return "".join(lis)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)