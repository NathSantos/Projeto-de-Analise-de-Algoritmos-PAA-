def seqSnake(M, l, c):
    matPD = [[0 for x in range(l+1)] for y in range(c+1)]
    maior_valor = 0

    # Montando a matriz de PD
    for i in range(0, l+1):
        for j in range(0, c+1):
            if(j > 0  and  abs(M[i][j] - M[i][j-1]) == 1):
                matPD[i][j] = max(matPD[i][j], matPD[i][j-1] + 1)
            if(i > 0  and  abs(M[i][j] - M[i-1][j]) == 1):
                matPD[i][j] = max(matPD[i][j], matPD[i-1][j] + 1)

            if(matPD[i][j] >= maior_valor):
                maior_valor = matPD[i][j]
    
    lista_sequencia = []
    posX = l
    posY = c
    flag = True

    # Percorrendo de volta o caminho da maior sequência de acordo com os valores na PD
    while(flag == True):
        lista_sequencia.append(M[posX][posY])

        if((matPD[posX][posY] - matPD[posX][posY-1] == 1) and (abs(M[posX][posY] - M[posX][posY-1]) == 1) and (matPD[posX][posY] != 0)):
            posY = posY-1
        elif((matPD[posX][posY] - matPD[posX-1][posY] == 1) and (abs(M[posX][posY] - M[posX-1][posY]) == 1) and (matPD[posX][posY] != 0)):
            posX = posX-1
        
        if(matPD[posX][posY] == 0):
            lista_sequencia.append(M[posX][posY])
            flag = False

    # Mostrando o resultado
    print(f"Tamanho máximo da cobra: {maior_valor}")
    print(f"Maior sequência: ", end="")
    for i in range(len(lista_sequencia)-1, -1, -1):
        if(i != 0): print(f"{lista_sequencia[i]} - ", end="")
        else:       print(f"{lista_sequencia[i]}")

# M sendo uma matriz NxN
M = [[7, 5, 2, 3, 1],
    [3, 4, 1, 4, 4],
    [1, 5, 6, 7, 8],
    [3, 4, 5, 8, 9],
    [3, 2, 2, 7, 6]]
l = len(M)-1
c = len(M)-1
seq = seqSnake(M, l, c)


'''
============= EXEMPLOS DE MATRIZES =============

-> EXEMPLO 1:
M = [[9, 6, 5, 2],
    [8, 7, 6, 5],
    [7, 3, 1, 6],
    [1, 1, 10, 7]]

SAÍDA ESPERADA:
Tamanho máximo da cobra: 6
Maior sequência: 9 - 8 - 7 - 6 - 5 - 6 - 7


-> EXEMPLO 2:
M = [[7, 5, 2, 3, 1],
    [3, 4, 1, 4, 4],
    [1, 5, 6, 7, 8],
    [3, 4, 5, 8, 9],
    [3, 2, 2, 7, 6]]

SAÍDA ESPERADA:
Tamanho máximo da cobra: 7
Maior sequência: 3 - 4 - 5 - 6 - 7 - 8 - 7 - 6

'''