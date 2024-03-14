def courseGrade():
    
    # TODO: Declare any necessary variables here. 
      
    midt1_sum = 0
    midt2_sum = 0
    fin_sum = 0  
    line_avg = 0
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
        with open(write_file, 'x'):
            for line in read_file:
                line = line.strip('\n')
                line_list = line.split("\t")
                midt1_sum += int(line_list[2])
                midt2_sum += int(line_list[3])
                fin_sum += int(line_list[4])
                line_avg = (line_list[2] + line_list[3] + line_list[4]) / 3
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
    print(write_file.read())
                

   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    return

if __name__ == "__main__":
    courseGrade()
    
    