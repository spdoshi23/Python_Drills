sentence = "python is fun and python is powerful"

lst = sentence.split(" ")
print(lst)

a = lst.count("python")
print(a)

b = lst.remove("fun")
c = lst.insert(2, "interesting")

sentence = " ".join(lst)
print(sentence)





