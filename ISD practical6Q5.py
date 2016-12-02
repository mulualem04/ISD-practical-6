sentence_1 = input("Enter a sentence: ")
sentence_2 = input("Enter a sentence: ")
# ask for sentence to enter
name = sentence_1 + " " + sentence_2
# concatenating sentences
print(name)
print(name.split())
myList = name.split()
# returns a list of all the words in the sentence
myList.sort()
# Sort items in a list in alphabetical order
print(len(myList))  
#Return the length (the number of items) in the list
for myList in myList:
    print(myList)
dic = {} # empty dictionary
for i in myList:
    dic.update({i: myList.count(i)}) # Add new entry
print(dic)   
