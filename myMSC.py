def msc(strA, strB, size):
    matPD = [[0 for x in range(size)] for y in range(size)]
    maior_valor = 0

    # Montando a matriz de PD
    for i in range(0, size):
        for j in range(0, size):

            if((i and j) > 0):

                if(strB[i] == strA[j]):
                    matPD[i][j] = matPD[i-1][j-1] + 1
                else:
                    matPD[i][j] = max(matPD[i][j-1], matPD[i-1][j])

            if(matPD[i][j] >= maior_valor):
                maior_valor = matPD[i][j]

    seq_msc = ""
    posX = size-1
    posY = size-1
    flag = True

    # Percorrendo de volta o caminho da maior sequência de acordo com os valores na PD
    while(flag == True):
        print(f"[{posX}],[{posY}]")

        # DIAGONAL (Letras iguais)
        if((matPD[posX][posY] - matPD[posX-1][posY-1] == 1) and (strB[posX] == strA[posY]) and (matPD[posX][posY] != 0)):
            seq_msc += strA[posY]
            posX = posX - 1 
            posY = posY - 1

        # PRA CIMA (Letras diferentes)
        elif((matPD[posX][posY] - matPD[posX-1][posY] == 0) and (strB[posX] != strA[posY]) and (matPD[posX][posY] != 0)):
            posX = posX-1

        # PRA ESQUERDA (Letras diferentes)
        elif((matPD[posX][posY] - matPD[posX][posY-1] == 0) and (strB[posX] != strA[posY]) and (matPD[posX][posY] != 0)):
            posY = posY-1
        
        if(matPD[posX][posY] == 0):
            flag = False

    # Mostrando o resultado
    print(f"Comprimento da MSC: {maior_valor}")
    print(f"MSC: ", end="")
    for i in range(len(seq_msc)-1, -1, -1):
        print(seq_msc[i], end="")


# StringA e StringB tendo o mesmo tamanho
stringA = "ACGTACGGGTA"
stringB = "GTCGATTTACG"
size = len(stringA)
msc(stringA, stringB, size)