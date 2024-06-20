import matrizlib

def Transpor(matriz):
    N_linhas = len(matriz)
    N_colunas = len(matriz[0])
    
    # Cria uma matriz transposta l x c inicializada com zeros
    matriz_transposta = [[0] * N_linhas for i in range(N_colunas)]
    
    # Preenche a matriz transposta
    for i in range(N_linhas):
        for j in range(N_colunas):
            matriz_transposta[j][i] = matriz[i][j]
    
    return matriz_transposta



def main():
    
    matriz = matrizlib.CriarMatriz()
    transposta = Transpor(matriz)

    print("Matriz original:")
    for linha in matriz:
        print(linha)
    
    print("\nMatriz transposta:")
    for linha in transposta:
        print(linha)


main()
