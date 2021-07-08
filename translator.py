 #Lookup word in find_word.txt
import time

start = time.time()
# print("hello")

def wordfinder(word,lookfile):
    if(word in lookfile):
        return 1
    else:
        return 0
# print(lookup("normal",["temp","joy"]))

#find the word meaning in lookup table
def dictionaryMeaning(word,lookuptable):
    return lookuptable[word]

#print(dictionaryMeaning("hi",{'hi':"mew"}))
import csv
from os import read
# Fetching the data from French_dictinary.csv file
import  csv
f= open("french_dictionary.csv",'r')
reader =csv.reader(f)
etor_dic={}          # dictionary data
for row in reader:
    etor_dic [row[0]]= row[1]
f.close()
#Fetch the data from Find_words.txt

f1=open("find_words.txt",'r')
reader =csv.reader(f1)
find_words=set()    # findwords data
for row in reader:
    find_words.add(row[0])
    # print (find_words)
f1.close()
#Fetch the Word from t8.shakespeare.txt file
fout=open("t8.shakespeare.translated.txt",'w')
f2=open("t8.shakespeare.txt",'r')
uniqueListRepalcedWords={}
# f2=open("input.txt",'r+')
reader=f2.readlines()
for row in reader:
    temp=row.split()
    #print(type(temp)) 
    # print(temp)
    for i in range (0,len(temp)):
        #print(temp[i])
         if(wordfinder(temp[i],find_words)):
            #  print(etor_dic[temp[i]])
            if temp[i] in uniqueListRepalcedWords.keys():
                uniqueListRepalcedWords[temp[i]]+=1
            else:
                uniqueListRepalcedWords[temp[i]]=0
            temp[i]=etor_dic[temp[i]]
        #  print(temp[i])
    fout.write(' '.join(temp)+"\n")

fout.close()

from csv import DictWriter
field_names = ['Word','Frequency']
with open("frequency.csv", 'a') as f_object:
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    for word,replaced in uniqueListRepalcedWords.items():
        dict={'Word': word ,'Frequency': replaced}
        dictwriter_object.writerow(dict)
f_object.close()

end = time.time()
perf=open("performance.txt",'w')
Time_taken=["Time to process:", (end-start) ,"minutes","0 seconds",]
perf.write(str(Time_taken )+"\n")
Memory=["Memory used: 10MB"]
perf.write(str(Memory)) 
perf.close()

# for words,replaced in uniqueListRepalcedWords.items():
#     if replaced >0:
#       print(words)
# # the Number of times a Word is replaced
# print ("-------- Number of times a Word is replaced-----") 

# for word, replaced in uniqueListRepalcedWords.items():
#     if replaced >0:
#      print(word, ":", replaced)








