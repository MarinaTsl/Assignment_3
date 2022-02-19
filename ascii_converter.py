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


