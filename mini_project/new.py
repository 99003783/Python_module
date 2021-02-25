import re
saw = int(input("enter the no. to search for words: \n"))
class search_w:

    def __init__(self):
        self.file_new=open(r"C:\Users\99003783\Documents\GitHub\Python_module\mini_project\input.txt")
        self.filter_str=self.file_new.read()
        self.word_search=input("enter the word:\n")
        self.file_save = self.word_search + '.txt'
        self.write_file = open(self.file_save, 'w+')

    def spilt(self):
        file_sp=self.filter_str.split()
        count = 0
        
        for i in range(len(file_sp)):
            word_search1 = re.match(self.word_search, file_sp[i], re.I|re.M)
            if word_search1:
                count+=1
                str78 = (file_sp[i-1] + ' ' + file_sp[i] + ' ' + file_sp[i+1])
                self.write_file.write(str(count) +  ':')
                self.write_file.write(str(str78) + '\n')
                
           
        self.write_file.write('no. of times word comes:' + str(count)+ '\n')
for i in range(saw):
    sample=search_w()
    sample.spilt()


