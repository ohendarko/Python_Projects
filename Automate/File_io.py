import os
"""
here = os.path.abspath('.')
print(here)
# here = os.path.isabs('.')
# print(here)
print(os.path.basename(here))
print(os.path.basename(os.getcwd()))
print(os.path.dirname(here))
print(os.path.split(here))
print(here.split(os.path.sep))
print(f"List of file strings")
for files in os.listdir(os.chdir('..')):
    print(files)
print(os.path.getsize(here))
"""
with open('Hello.txt', 'r') as f:

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())
    #while len(f_contents) > 0:
    #    print(f_contents, end='*')
    #    f_contents = f.read(size_to_read)


