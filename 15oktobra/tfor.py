f = open("tword.txt", "r")
print("{0:-^100s}".format("статья"))
for c in f.readlines():
    print("{0:-^100s}".format(c))