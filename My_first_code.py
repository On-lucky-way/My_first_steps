F = open("save_logs.txt", "w")

with open('C:\\Users\Пользователь\Desktop\log.txt') as file:
    lines_list = file.readlines()
    for line in lines_list:
        code = line.split(', ')
        print(code[0])
        print(code[2])
F.write(code[0])
F.write(code[2])
F.close()
