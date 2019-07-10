file=open("Effects.txt", "r")
f1 = file.readlines()
file.close()

count = 0

li = []

for line in f1:
    j=0
    line = line.strip()
    # print(x)
    for element in line:
        if element != ',':
            print(element)
            li[count] += element
        else:
            j+=1
    count += 1
