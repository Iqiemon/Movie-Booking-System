def movieList():
	file = open("MovieList.txt", encoding="utf8")
	print(file.read())
	file.close()