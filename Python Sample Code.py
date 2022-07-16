# This is a sample Python script.

###Categorizing based on age:
import pandas as pd
import numpy as np
from collections import Counter
def AgeCategory():

    Age_data = pd.DataFrame({'Age': [12, 5, 28, 89, 90, 34, 45]})
    bins = [0, 2, 4, 13, 20, 60, np.inf]
    labels = ['Infant', 'Toddler', 'Kid', 'Teen', 'Adult', 'Senior Citizens']
    Age_data['AgeGroup'] = pd.cut(Age_data['Age'], bins=bins, labels=labels, right=False)
    print(Age_data)

AgeCategory()

###Anagram strings:

def anagram():
    str1 = "listen"
    str2 = "silent"

    print(sorted(str1))
    print(sorted(str2))
    print(Counter(str1))
    print(Counter(str2))
    if(sorted(str1) == sorted(str2)):
        print("String are Anagram")
    else:
        print("String are not Anagram")

anagram()

####Reverse the string
# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string

s = "Geeksforgeeks"
print("The original string is : ", end="")
print(s)
print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))

#####Reverese the Words in sentence

# Python code
# To reverse words in a given string
def ReverseString(string):

    # reversing words in a given string
    s = string.split()[::-1]
    # l = []
    # for i in s:
    #     # apending reversed words to l
    #     l.append(i)
    # printing reverse words
    print(" ".join(s))

# input string
string = "geeks quiz practice code"
print ("Original String is : ",string)
ReverseString(string)