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
    #If it is a string of alphabetical characters, check to see if it's length plus the previous' length equals 20
    elif (len(words[i])+len(words[i-1])==20):
        words.pop(words[i]); words.pop(words[i-1])


    


