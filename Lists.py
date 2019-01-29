# indexing
# Create a list
L = ["Micheal Jackson",10.1,1982]
print(L)

# we can use both postive and negative indexing
# Print the elements of each index
print('the same element using both positive and negative indexing:\n Positive: ',L[0],'\n Negative: ',L[-3])
print('the same element using both positive and negative indexing:\n Positive: ',L[1],'\n Negative: ',L[-2])
print('the same element using both positive and negative indexing:\n Positive: ',L[2],'\n Negative: ',L[-1])

# List Content
# Sample List
L = ["Micheal Jackson",10.1,1982,"MJ",1]
# list slicing
print(L[3:5])
# use extend to add elements to list
L = ["Micheal Jackson",10.2]
L.extend(['pop',10])
print(L)
#use append to add elements to the list
L = ["Micheal Jackson",10.2]
L.append(['pop',10])
print(L)
# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)
# Use append to add elements to list
L.append(['a','b'])
print(L)

#change the first element of list
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

#delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space
print('hard rock'.split())

# Split the string by comma
print('A,B,C,D'.split(','))

# Copy and Clone List
# Copy (copy by reference) the list A
A = ["hard rock",10,1.2]
B = A
print('A: ', A)
print('B: ', B)

#Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]', B[0])

# Clone (clone by value) the list A
B = A[:]
print(B)

# Now, change A, B will not change
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

# Quiz on list
# Create a list a_list, with the following elements 1, hello, [1,2,3] and True
a_list = [1,"hell0",[1,2,3],True]
print(a_list)

# Find the value stored at index 1 of a_list
print(a_list[0])

# Retrieve the elements stored at index 1, 2 and 3 of a_list
print(a_list[1:4])

# Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']
A = [1,'a']
B = [2,1,'d']
print(A+B)