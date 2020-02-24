with open("a_example.txt", "r") as file:
    linha1 = file.readline().split()
    days = int(linha1[0])
    totallib = int(linha1[1])
    libraries = []
    scores = [int(i) for i in file.readline().split()]
    for i in range(totallib):
        lib = [int(i) for i in file.readline().split()[1:3]]
        lib.append([int(i) for i in file.readline().split()])
        lib.insert(0, i)
        libraries.append(lib)
file.close()

