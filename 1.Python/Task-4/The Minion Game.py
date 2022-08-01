def minion_game(string):
    # your code goes here
    Stuart,Kevin = 0,0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            Kevin+=(len(string) - i)
        else:
            Stuart+=(len(string) - i)
    if Stuart == Kevin:
        print('Draw')
    if Stuart > Kevin:
        print('Stuart {}'.format(Stuart))
    if Stuart < Kevin:
        print('Kevin {}'.format(Kevin))  

if __name__ == '__main__':
    s = input()
    minion_game(s)