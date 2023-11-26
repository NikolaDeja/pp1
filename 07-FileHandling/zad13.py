movie_titles =["A","B","C"]


file=open("movies.txt", "w")
for i in movie_titles:
    file.write(i+"\n")

file.close()