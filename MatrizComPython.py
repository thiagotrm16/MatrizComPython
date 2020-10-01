#Capturara quantidade de linhas e colunas
l = int(input("Digite a quantidade de linhas: "))
c = int(input("Digite a quantidade de colunas: "))

#Verificar o tamanho das linhas e colunas
if (l<=20) and (c<=20):
    #Comandos para criar a matriz
    matriz = []
    elemento = 1
    for linha in range(l):
        matriz.append([])
        for coluna in range(c):
            matriz[linha].append(elemento)
            elemento+=1
        
    #Comandos para exibir a matriz
    j = 0
    y = 0
    while j < l:
        print("|", end="")
        while y < c:
            print("{0:3}" .format(matriz[j][y]), end="  ")
            y+=1
        j+=1
        y=0
        print("|", end="")
        print("")
else:
    print("Não é permitido que as linhas ou colunas tenham mais do que vinte elementos")
