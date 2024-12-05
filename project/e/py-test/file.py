import os
import shutil


# path = "/home/hicri/Masaüstü/py-test/test-file"
#
# if os.path.exists(path):
#     print("exist")
#     if os.path.isfile(path):
#         print("this is file")
#     elif os.path.isdir(path):
#         print("this is director")
# else:
#     print("no exist")

# try:
#     with open("./test-file/text.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("not found")


# text = "yoooooooooooooooo\n what's up bro"
#
# with open("./test-file/text.txt", 'w') as file:
#     file.write(text)

#
# shutil.copyfile('test-file/text.txt', 'test-file/copy.txt') #src, dst


# source = "/home/hicri/Masaüstü/py-test/test-file/"
# destination = "/home/hicri/Masaüstü/py-test/copy-file"
#
#
# try:
#     os.replace(source, destination)
#     print("move")
#
# except FileNotFoundError:
#     print("Not Found")

# path = "/home/hicri/Masaüstü/py-test/copy-file/text.txt"
#
# try:
#     os.remove(path) # delete a file
#     os.rmdir(path) # delete a empty directory
#     shutil.rmtree(path) # combo delete
# except FileNotFoundError:
#     print("file is not exist")