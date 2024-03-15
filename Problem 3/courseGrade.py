def courseGrade():
    '''
    Name: Wyatt Fulton
    Date: Thur 2:00 PM
    '''
      
    midt1_sum = 0
    midt2_sum = 0
    fin_sum = 0
    midt1_avg = 0
    midt2_avg = 0
    fin_avg = 0  
    line_avg = 0
    num_lines = 0
    line_grade = ''
    file_name = input()
    write_file = ''


    if file_name == './Problem 3/StudentInfo.tsv':
        write_file = './Problem 3/report.txt'
    elif file_name == './Problem 3/StudentInfo1.tsv':
        write_file = './Problem 3/report1.txt'
    else:
        write_file = './Problem 3/report2.txt'


    with open(file_name, 'r') as read_file:
        with open(write_file, 'w') as write_file:
            for line in read_file:
                line = line.strip('\n')
                line_list = line.split()
                midt1_sum += int(line_list[2])
                midt2_sum += int(line_list[3])
                fin_sum += int(line_list[4])
                line_avg = (int(line_list[2]) + int(line_list[3]) + int(line_list[4])) / 3
                if line_avg >= 90:
                    line_grade = 'A'
                elif (line_avg < 90) and (line_avg >= 80):
                    line_grade = 'B'
                elif (line_avg < 80) and (line_avg >= 70):
                    line_grade = 'C'
                elif (line_avg < 70) and (line_avg >= 60):
                    line_grade = 'D'
                else:
                    line_grade = 'F'
                write_file.write(str(line_list[0])+'\t'+str(line_list[1])+'\t'+str(line_list[2])+'\t'+str(line_list[3])+'\t'+str(line_list[4])+'\t'+line_grade+'\n')
                num_lines += 1
            midt1_avg = float(midt1_sum / num_lines)
            midt2_avg = float(midt2_sum / num_lines)
            fin_avg = float(fin_sum / num_lines)
            write_file.write(f"Averages: midterm1 {midt1_avg:.2f}, midterm2 {midt2_avg:.2f}, final {fin_avg:.2f}\n")
                

    return

if __name__ == "__main__":
    courseGrade()



    
    