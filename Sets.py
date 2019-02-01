# Create a set
set1 = {"pop","rock","soul","hard rock","soft rock","rock","R&B","rock","disco"}
print(set1)

# Convert list to set
album_list = ["Micheal Jackson","Thriller",1982,"00:42:19", \
    "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_list = set(album_list)
print(album_list)

# Convert list to set
music_genres = set(["pop","pop","rock","folk rock","hard rock","soul",\
    "progressive rock","soft rock","R&B","disco"])
print(music_genres)

# Set Operations
# Sample Set
A = set(["Thriller","Back in Black","AC/DC"])
print(A)

# Add element to set
A.add("NSNYC")
print(A)

# try adding dupllcate element to the set
A.add("NSNYC")
print(A)

# remove an element from the set
A.remove("NSNYC")
print(A)

# Verify if teh element is in the set
print('AC/DC' in A)
print('NSNYC'in A)

# Set Operations

