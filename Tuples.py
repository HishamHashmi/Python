#create your 1st tuple
tuple1 = ("disco",10,1.2)
tuple1

#print tuple type
type(tuple1)

#indexing

#print variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

#print type of variable on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

#use negative index to get the value of the last element
print(tuple1[-1])

#use negative index to get the value of the second last element
print(tuple1[-2])

#use negative index to get the value of the third last element
print(tuple1[-3])

#Concatenate tuple

#Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

#Slicing

#Slice from index 0 to 2
print(tuple2[0:3])

#Slice from index 3 to 4
print(tuple2[3:5])

#get the length of tuple
print(len(tuple2))

#Sorting

#A sample tuple
Ratings = (0,9,6,5,10,8,9,6,2)
print(Ratings)
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

#Nested Tuple
#Create a nested tuple
Nested1 = (1,2,("pop","rock"),(3,5),("disco",(1,2)))
print(Nested1)
#print element on each index 
print("Element 0 of Tuple",Nested1[0])
print("Element 1 of Tuple",Nested1[1])
print("Element 2 of Tuple",Nested1[2])
print("Element 3 of Tuple",Nested1[3])
print("Element 4 of Tuple",Nested1[4])

