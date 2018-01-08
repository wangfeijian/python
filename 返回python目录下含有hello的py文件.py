import os
file = []
def search_file(dir_m,filedir):
    file_abspath = os.path.join(dir_m, filedir)
    if os.path.isdir(file_abspath):
        alldirfile = os.listdir(file_abspath)
        for f in alldirfile:
            search_file(file_abspath,f)
    else:
        if file_abspath.endswith(".py"):
            if read_line(file_abspath):
                file.append(file_abspath)

def read_line(filedir):
    flag = False
    f = open(filedir, encoding='UTF-8')
    while True:
        line = f.readline()
        if line == '':
            break
        elif "turtle" in line:
            flag = True
            break
    # print(flag)
    f.close()
    return flag

search_file("E:\编程语言","Python")
print(file)