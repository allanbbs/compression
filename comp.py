
def get_key(my_dict,val):
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return None


file = open("alice29.txt","r")
content = file.readlines()
print(content)
d = {}
mask = 1
result = []
bro = []
for line in content:
	bro = []
	l_cont = line.split()
	for word in l_cont:
		if d.get(word):
			bro.append(str(d.get(word)))
		else:
			d[word] = str(mask)
			bro.append(str(mask))
			mask+=1
	result.append(bro)
print(result)
decomp = []
res2=[]
for x in result:
	decomp = []
	for y in x:
		actual = get_key(d,y)
		decomp.append(actual)
	res2.append(decomp)
out = open("compressed.txt","w+")
dic = open("dict.txt","w+")
dic_line = []
for i,j in d.items():
	dic_line.append(str(i)+":"+j)
dic.write(" ".join(dic_line))
dic.write("\n")
for line in result:
	l = " ".join(line)
	out.write(l)
	out.write("\n")
out.close()
file.close()



