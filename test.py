dados = []
tupla = []

tupla.append("1")
tupla.append("IDE")
tupla.append("a")
dados.append(tupla)
tupla = []
tupla.append("2")
tupla.append("IDE")
tupla.append("b")
dados.append(tupla)
tupla = []
tupla.append("3")
tupla.append("IDE")
tupla.append("c")
dados.append(tupla)
tupla = []

for x in range(len(dados)):
    for y in range(len(dados[x])):
        print(dados[x][y])