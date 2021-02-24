import re

count = 0
str_output=[]
line=0



#print(range(pattern))

qwe = input("enter the first keyword: ")


with open(".\mini_project\input.txt",'r') as f_io:
    for line in f_io:
        if qwe in line:
            
             print(line, end=" ")




wqa = re.findall(qwe,f_io,re.M|re.I)



#print(der)
#print(len(der))this



'''for fde in rewq:
    
    lines+=1
    print(fde,end=' ')
if len(qwe) != None:
    l.append((lines,qwe.rstrip('\n')))'''


for answer in wqa:   
    count+=1
with open(qwe +".txt",'a') as file_answer:
        file_answer.writelines(str(count) + ' :')
        file_answer.writelines(answer[1] + '\n')




#for answer in qwe:
  #  count+=1
#with open("qwe.txt",'a') as file_answer:
 #       file_answer.writelines(str(count)+' :')
  #      file_answer.writelines(answer[1]+ '\n')



    

