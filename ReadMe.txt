
File structure
1. input file is "t8.shakespeare.txt"
2. output Files "t8.shakespeare.translated.txt",perfornmance.txt file, Frequency.csv file.
How to run the program
1.first check the t8.shakespeare.translated.txt, perfornmance.txt , Frequency.csv which shoud be empty initially.If they are not empty So Delete all the data from all the files 
2. Now click on run the program
Output formate:
1. translated Text is appear in t8.shakespeare.translated.txt file
2.Perfrormance is appear in perfornmance.txt file
3.How many Time a word is repalced during Translation is appear in Frequency.csv file


Total Memory Uses:
Used Memory
1.Dictonary to store the key Value Pairs O(number of words in dictionary)
2. set is used for storing the find_word file content - O(number of unique word in find_word file)
3.uniqueListRepalcedWords to store the repalced data - O(number of repalced word) 


Total Time is Used
1.  O(Number of Rows * Number of words in each Row) in the input file(t8.shakespeare.txt)
2. to searching time in a set which is logN (for the N values) for find word in find_word file
3. and Constact time to search a value for a corresponding word in french_dic file

