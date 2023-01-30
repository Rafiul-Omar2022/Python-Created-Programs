# Author: Rafiul Omar  
# Date : 31/01/2023
# Program: Python, search word form sentences and output word starting index and last index. 

# Warning: Just search only words, examples, "I am Rafiulomar". in this sentences search only words like "am"/"I"/"Rafiulomar". Error search, "Rafi"/"I "/"a"/"omar" .


# This code is for taking input from a user and store is to another variable which is called messageClone.
# Created a seperated sentences array/list to append words from message.
message  = input("Type something...: ")
messageClone = message
message += " "
words = ""
sentences = []

for i in message:
    if(i == " "):
        sentences.append(words)
        words = ""
    else:
        words += i


# This code take a searching input to search in a sentences 
name  = input("Search in text string: ")

wordCounter = 0  # Golbal word count
s = 0 # s stands for  counting the spaces between two words 

for i in sentences:
    wordCounter += len(i)
    s += 1
    if(name == i):
        sp = s + wordCounter - len(i) 
        break

print(f"So position will be in from index {sp-1} to {wordCounter + s - 2}.")  # This line is showing the output of searching word starting to ending indexes
        



