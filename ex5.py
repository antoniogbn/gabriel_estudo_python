import matrizlib

def DiagonalPrincipal(M):
    N_linhas = len(M)
    diagonal = [M[i][i] for i in range(N_linhas)]
    return diagonal

def main():
    # Exemplo de matriz quadrada (substitua com os valores reais)
    matriz = matrizlib.CriarMatriz()
    diagonal = DiagonalPrincipal(matriz)
    print(f'A diagonal principal é: {diagonal}')

main()

    
    
