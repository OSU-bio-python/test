data = file("Weakley_plant_list_workshop.csv", "r").readlines()
outfile = file("pinaceae.txt","w")
mydict = {}
for line in data:
    linelist = line.split(",")
    if linelist[1] != '':
        mydict[linelist[0]] = linelist[1]
x = mydict.keys()
z = 0
for i in x:
   if mydict[i] == 'Pinaceae':
       outfile.write(i+"\n")
       z = z +1
outfile.close()
print z

