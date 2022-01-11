fhand = open('employee.txt', 'w')
columns = 'emp.no, emp.name, emp.address, dept, salary, experience\n'
fhand.write(columns)
fhand.close()
fhand1 = open('employee.txt', 'a')
yes_no = input('do you want to enter information(yes/no): ')
while yes_no == 'yes':
    emp_no = int(input('enter employee number: '))
    emp_name = input('employees name: ')
    emp_add = input('enter address: ')
    emp_dept = input('enter department: ')
    emp_sal = input('enter Salary: ')
    experience = input('experience: ')
    line = f'{emp_no}, {emp_name}, {emp_add}, {emp_dept}, {emp_sal}, {experience}'
    fhand1.write(f'{line}\n')
    yes_no = input('do you want to enter information(yes/no): ')
else:
     fhand1.close()

info_dict = {}
with open('employee.txt', 'r') as file:
    information = file.readlines()[1:]
    for line in information:
        info_line = line.rstrip().split(',')
        info_dict[info_line[0]] = {
            'name': info_line[1],
            'address':info_line[2],
            'dept': info_line[3],
            'salary':int(info_line[4]),
            'experience': int(info_line[5]),
        }
# getting employee name with salary above 50000 from same department and same years of experience
l_salary = []
l_dept = []
l_exp = []
for key in info_dict:
    if info_dict[key]['salary'] > 50000:
        l_salary.append(info_dict[key]['name'])
    if info_dict[key]['dept'].lstrip() == 'mechanical':
        l_dept.append(info_dict[key]['name'])
    if info_dict[key]['experience'] == 5:
        l_exp.append(info_dict[key]['name'])

print(f'employees with salary above 50000 is {l_salary}')
print(f'employees from mechanical department is {l_dept}')
print(f'employees with same years of experience is {l_exp}')





