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

