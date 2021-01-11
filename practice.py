student_file = open("student", "r+")
student =student_file.readlines()
student_file.seek(0)
for line in student:
    name=line.split("|",1)
    print(name)
    if "Yash" not in line:
        student_file.write(line)
student_file.truncate()