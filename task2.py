#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
lst=['']
x=(input("enter a word=>")).strip()
y=(input("enter a word=>")).strip()
z=(input("enter a word=>")).strip()
c=(input("enter a word=>")).strip()
v=(input("enter a word=>")).strip()
lst.append(x)
lst.append(y)
lst.append(z)
lst.append(c)
lst.append(v)

print(lst)