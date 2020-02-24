def get_key(my_dict,val):
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return None
file = open("compressed.txt","r")
dic = open("dict.txt","r")
d = {}
dic_line = dic.readline()
for x in dic_line.split():
	item = x.split(":")
	d[item[0]] = item[1]



res2 = []
bro = []
f = open("decompressed.txt","w+")
for line in file.readlines():
	res2=[]
	result = line.split()
	for x in result:
		actual = get_key(d,x)
		res2.append(actual)
	bro.append(res2)

for line in bro:
	f.write(" ".join(line))
	f.write("\n")
file.close()
f.close()
#print(res2)