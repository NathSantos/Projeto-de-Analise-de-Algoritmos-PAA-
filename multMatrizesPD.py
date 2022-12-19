def multMatrizPD(d, size):
    matPD = [[0 for x in range(size)] for y in range(size)]
    matK = [[0 for x in range(size)] for y in range(size)]

    jIniciais = [i for i in range(1, size)]
    
    for j in range(len(jIniciais)):
        j_aux = j+1
        for i in range(len(jIniciais)):
            print(f"[{i}],[{j_aux}]")

            
            j_aux+=1


        jIniciais.pop(0)

d = [10,20,3,4,30]
size = len(d)-1
multMatrizPD(d, size)
