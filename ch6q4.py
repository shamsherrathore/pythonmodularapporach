a = "hey how are you"
l = a.split()
for c in range(len(l)):
    l[c] = l[c].title()

print(" ".join(l))
