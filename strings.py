#defining string
"Hisham Hashmi"
#assign string to variables
Name = "Hisham Hashmi"
Name

#indexing
print(Name[0])
print(Name[4])
print(Name[10])

#negative indexing
print("Negative Indexing")
print(Name[-1])
print(Name[-5])
print(Name[-13])

#slicing
print("Slicing")
print(Name[0:4])
print(Name[8:12])

#stride
print("Stride")
print(Name[::2])

#concatenate
Name = Name + " python pratice"
print(Name)

#print string multiple times
print (3 * "hisham hashmi")

#concatenate string
statement = Name + " repository"
print (statement)

#Escape Sequence
print("Hisham Hashmi's \n python repository")
print("Hisham Hashmi's \t python repository")
print("Hisham Hashmi's \\ python repository")

#String Operations

#Convert all the characters in string to upper case
A = "Thriller is the sixth album studio"
print("before upper:", A)
B = A.upper()
print("after upper:", B)

#Replace the old substring with the new target substring is the segment has been found in the string
A = "Micheal Jackson is the best"
B = A.replace('Micheal','Janet')
print (B)

#Find the substring in the string. Only the index of the first elment of substring in string will be the output
Name = "Micheal Jackson"
Name.find('el')
Name.find('Jack')
Name.find('Jasdfasdasdf')

F = "You are wrong"
D = F.upper()
print(D)
