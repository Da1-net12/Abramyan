f1 = open("input.txt", "r")
a = int(f1.readline())
print(a)
b = int(f1.readline())
for line in f1:
    print(line.strip())
f1.close

r = str(a+b)

f2 = open("output.txt","w")
f2.write(r)
f2.close()


