'''
Name: Wyatt Fulton
Lab Time: Thur 2:00 PM
'''

#def wordInRange():
    inp_file = input()
    start_line = input()
    stop_bound = input()
    with open(inp_file, 'r') as current_line:
        for line in current_line:
            line = line.strip('\n')
            if line >= start_line:
                if line <= stop_bound:
                    print(line + ' - in range')
                else:
                    print(line+' - not in range')
            else:
                print(line+' - not in range')


    return
if __name__ == '__main__':
    wordInRange()