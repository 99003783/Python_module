import re

count = 0

qwe = input("enter the first keyword")
l = qwe.split()

pattern = re.compile(qwe,re.I|re.M)
print(range(pattern))

with open(".\mini_project\input.txt",'r') as f_io:
    for line in f_io:
        if qwe in line:
            print(line)
            
for 



#print(der)
#print(len(der))this



'''for fde in rewq:
    
    lines+=1
    print(fde,end=' ')
if len(qwe) != None:
    l.append((lines,qwe.rstrip('\n')))'''


for answer in pattern:   
    count+=1
with open(qwe +".txt",'a') as file_answer:
        file_answer.writelines(str(count) + ' :')
        file_answer.writelines(answer[1] + '\n')




#for answer in qwe:
  #  count+=1
#with open("qwe.txt",'a') as file_answer:
 #       file_answer.writelines(str(count)+' :')
  #      file_answer.writelines(answer[1]+ '\n')



    

