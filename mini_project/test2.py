import re

count = 0
loop1 = int(input("Enter number of words what you want to search in the file:"))
for j in range(0,loop1):
         count=0
line=0
result=[]
word=str(input("enter words {}:".format(j+1)))
patt=re.compile(word,re.I)
with open('./mini_project\input.txt','rt') as file_info:
            for file_line in file_info:
                line=line+1
                if patt.search(file_line) is not None:
                    result.append((line,file_line.strip('\n')))
            
            for answer in result:
                count=count+1

                with open("{}.txt".format(word),'a') as file_answer:
                    file_answer.writelines(str(count)+' :')
                    file_answer.writelines(answer[1]+'\n')
                   
print(count)