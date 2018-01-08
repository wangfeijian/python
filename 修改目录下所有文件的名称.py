import os
# file = []
file_abspath = os.path.abspath("rename")
# print(file_abspath)
for f in os.listdir(file_abspath):
    file = os.path.join(file_abspath,f)
    ref = "re-" + f
    os.rename(file,os.path.join(file_abspath,ref))
# print(file)
