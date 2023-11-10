import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore test\nAnd more")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())


os.rename("mydata.txt", "mydata2.txt")
os.remove("mydata2.txt")
# os.mkdir("mydir")
os.chdir("mydir")
print("Current Directory :", os.getcwd())
os.chdir("..")
print("Current Directory :", os.getcwd())
os.rmdir("mydir")