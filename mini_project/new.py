import re
file_new=open(r"C:\Users\99003783\Documents\GitHub\Python_module\mini_project\input.txt")

count = 0

filter_str=file_new.read()
word_search=input("enter the word:\n")

no_of_times=re.findall(word_search,filter_str, re.M|re.I)

file_sp=filter_str.split()

file_save = word_search + '.txt'
write_file = open(file_save, 'w+')
for i in range(len(file_sp)):
    word_search1 = re.match(word_search, file_sp[i], re.I|re.M)
    if word_search1:
       count+=1

       str78 = (file_sp[i-1] + ' ' + file_sp[i] + ' ' + file_sp[i+1])
       write_file.write(str(str78) + '\n')
       write_file.write(str(count) +  ':')

write_file.write('no. of times word comes:' + str(len(no_of_times)) + '\n')
