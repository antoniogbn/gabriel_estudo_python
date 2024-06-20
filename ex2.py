import matrizlib
'''
Função que identifica os elementos pares na Matriz estabelecida
Entradas: Matriz (Lista) -> Pares(INT)
'''
def IdenPares(Par):
    #define o numero de linhas e colunas para a matriz dada
    N_linhas = len(Par)
    N_colunas = len(Par[0])
    
    #Define a quantidade de pares
    Pares = 0
    #Varredura da matriz
    for i in range(N_linhas):
        for j in range(N_colunas):
            #verifica se o elemento em questão é par
            if Par[i][j] % 2 == 0:
                Pares += 1
    return Pares

def main():
    Matriz = matrizlib.CriarMatriz()
    ParesF = IdenPares(Matriz)
    print (f'A matriz possui {ParesF} pares.')

main()
    
