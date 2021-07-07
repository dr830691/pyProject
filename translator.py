#Lookup word in find_word.txt
def wordfinder(word,lookfile):
    if(word in lookfile):
        return 1
    else:
        return 0
#print(lookup("normal",["temp","joy"]))
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
find_words=[]     # findwords data
for row in reader:
    find_words.append(row[0])
    # print (find_words)
f1.close()
print(wordfinder("project",find_words))
#Fetch the Word from t8.shakespeare.txt file
# fout=open("out.txt",'wt')
# f2=open("t8.shakespeare.txt",'r+')
# reader=f2.readlines()
# for row in reader:
#     temp=list(row)
#     for lookup in temp:
#         if(wordfinder(lookup.lower(),find_words)):
#             temp.repalce("Project",etor_dic['project'])
#             fout.write(temp)
# print(temp)
        
            
   










