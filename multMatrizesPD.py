def multMatrizPD(d, size):
    matPD = [[0 for x in range(size)] for y in range(size)]
    matK = [[0 for x in range(size)] for y in range(size)]

    jIniciais = [i for i in range(1, size)] # guarda os valores de j's (colunas) iniciais de cada diagonal que deve ser lida  
    
    for j_aux in range(len(jIniciais)):
        j = j_aux+1
        for i in range(len(jIniciais)):
            valoresM_K = {}

            for k in range(i, j):
                valoresM_K[matPD[i][k] + matPD[k+1][j] + (d[i]*d[k+1]*d[j+1])] = k+1

            menor_valor = min(valoresM_K.keys())
            valor_k = valoresM_K.get(menor_valor)

            matPD[i][j] = menor_valor
            matK[i][j] = valor_k
            
            j+=1
        jIniciais.pop(0)

    print("===== Matriz de valores PD: =====")
    for i in range(len(matPD)):
        print(matPD[i])

    print("===== Matriz de escolhas K: =====")
    for i in range(len(matK)):
        print(matK[i])

d = [10,20,3,5,30,4]
size = len(d)-1
multMatrizPD(d, size)
