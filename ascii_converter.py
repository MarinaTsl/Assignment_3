#To read the .txt file:
file=open("two_cities_ascii.txt")
txt=file.read()

#To split the given text: 
words = txt.split()

#For every word on the list
for i in range(len(words)):
    #If it is not string of alphabetical characters, pop it out of the list
    if (words[i].isalpha()==False):
        words.pop(words[i])       

    #Else, if it is a word shorter than 20 characters: 
    elif (i>0 and len(words[i])<20):
        #Search the already checked part of the list 
        for k in range(i):
           #for a word whose length plus the current word's length is 20
            if(len(words[i])+len(words[k])==20):
                #If found, pop the word
                words.pop(words[i]); words.pop(words[k])
                break

#To find the length of the longest word:
longest_word=0
for i in range(len(words)):
    if(len(words[i])>longest_word):
        longest_word=len(words[i])

stats=[]

for i in range(len(words)):
    
    #Word length counter initialization:
    if (i<longest_word):
        stats[i]=0
    
    stats[len(words[i])-1]+=1

#Printing the statistics:
for i in range(longest_word): 
    if (stats[i]==1):
        print("1 {} letter word".format(i+1))
    else:
        print("{} {} letter words ".format(stats[i], i+1))








