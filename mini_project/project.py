import re


count = 0
lines = 0

rewq = open(r"C:\Users\99003783\Documents\GitHub\Python_module\mini_project\input.txt") 
filename= rewq.read()
qwe = input("enter the first keyword")
l = list(qwe)

pattern = re.findall(qwe,filename,re.M|re.I)

#print(der)
#print(len(der))this



for fde in filename:
    
    lines+=1
    print(fde)
if len(qwe) != None:
    l.append((lines,qwe.rstrip('\n')))


for answer in pattern:   
    count+=1
with open(qwe +".txt",'a') as file_answer:
        file_answer.writelines(str(count)+' :')
        file_answer.writelines(answer[0]+ '\n')




#for answer in qwe:
  #  count+=1
#with open("qwe.txt",'a') as file_answer:
 #       file_answer.writelines(str(count)+' :')
  #      file_answer.writelines(answer[1]+ '\n')



    

