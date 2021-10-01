f1 = open("input.txt", "r")
a = int(f1.readline())
b = int(f1.readline())
for line in f1:
    print(line.strip())
f1.close

f2 = open("output.txt","w")

if a < b:
        f2.write("<")
if a > b:
        f2.write(">")
if a == b:
        f2.write("=")
f2.close()