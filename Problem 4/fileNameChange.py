'''
Name: Wyatt Fulton
Lab Time: Thur 2:00 PM
'''

def fileNameChange():
    
    file_name = input()
    updated_file = file_name
    accumulator = 0
    newfile_list = []


    with open(file_name, '+r') as file_name:
        for line in file_name:
            line = str(line).split("_")
            update_line = line[0]+'_info.txt\n'
            newfile_list.append(update_line)

    with open(updated_file, 'w') as updated_file:
        for i in newfile_list:
            updated_file.write(i)
            

    return

if __name__ == '__main__':
    fileNameChange()