def print_formatted(number):
    # your code goes here
    leng = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(leng," "),end = " ")
        print(str(oct(i)[2:]).rjust(leng," "),end = " ")
        print(str(hex(i)[2:]).upper().rjust(leng," "),end = " ")
        print(str(bin(i)[2:]).rjust(leng," "))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)