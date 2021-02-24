import re
word = input("enter the word")
f_r =open(r"C:\\Users\\99003783\\Documents\\GitHub\\Python_module\\mini_project\\input.txt") 
f= f_r.read()
count = re.findall(word, f, re.M | re.I)
print(len(count))
#file2=open('a',"C:\Users\9003783\Documents\GitHub\Python_module\mini_project\output_file.txt")
#file2.write(len(count))