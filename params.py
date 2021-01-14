# сервисный аккаунт, который будет осуществлять действия в аккаунте
# credentials.json аккаунта должны лежать рядом со скриптом
teacher_mail = 'onlineeducation@miem.hse.ru'

# название курса как в классруме 
course_name = 'лёша'

# название задания в классруме
# внимание!!! задание должно быть создано с помощью файла make_assignment.py
assignment_name = '12345'

# здесь что-то типа почты ученика
student_mail = 'asshadrunov@miem.hse.ru'

# префикс в названии файла hw1-asshadrunov.ipynb
grade_name = 'hw1'

# паттерны
student_file = f"hw1_{student_mail.split(r'@')[0]}.ipynb"
grade_file = f"hw1_{student_mail.split(r'@')[0]}_graded.ipynb"

