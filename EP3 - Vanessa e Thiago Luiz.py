

entrada1 = '''
010
111
000
101'''

entrada2 = '''
10101
10101
11111'''

entrada3 = '''
0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110'''

resultado1 = []
resultado2 = []
resultado3 = []

def main():
    global entrada1, resultado1, entrada2, resultado2, entrada3, resultado3

    resultado1 = tratando_entradas(entrada1, resultado1)
    resultado1 = verifica_vizinhos(resultado1)

    resultado2 = tratando_entradas(entrada2, resultado2)
    resultado2 = verifica_vizinhos(resultado2)

    resultado3 = tratando_entradas(entrada3, resultado3)
    resultado3 = verifica_vizinhos(resultado3)

    print("Entrada:",entrada1)
    print("\nSaída:", imprimir_matriz(resultado1))
    print("\n")
    print("Entrada:",entrada2)
    print("\nSaída:", imprimir_matriz(resultado2))
    print("\n")
    print("Entrada:",entrada3)
    print("\nSaída:", imprimir_matriz(resultado3))

def imprimir_matriz(resultado):
    matriz = ''
    for x in resultado:
        linha = "".join(str(x) for x in x)
        matriz = matriz + "\n" + linha
    
    return matriz

def tratando_entradas(entrada, resultado):
    resultado = entrada.split()
    temp = []
    for x in resultado:
        temp.append([int(x[i:i+1]) for i in range(0, len(x), 1)])
    resultado = temp
    return resultado


def verifica_vizinhos(resultado):
    rotulo_atual = 0
    altura = len(resultado)
    largura = len(resultado[0])

    for x in range(0, altura):
        for y in range(0, largura):
            if x == 0 and y == 0 :
                if resultado[x][y] == 0:
                    continue
                else:
                    rotulo_atual = rotulo_atual + 1
                    resultado[x][y] = rotulo_atual
            elif x == 0 and y > 0:
                if resultado[x][y] == 1:
                    vizinho_esquerda = resultado[x][y-1]
                    if vizinho_esquerda == 0:
                        rotulo_atual = rotulo_atual + 1
                        resultado[x][y] = rotulo_atual
                    elif vizinho_esquerda == rotulo_atual:
                        resultado[x][y] = rotulo_atual
                else:
                    continue
            elif x > 0 and y==0:
                if resultado[x][y] == 1:
                    vizinho_cima = resultado[x-1][y]
                    if vizinho_cima > 0:
                        resultado[x][y] = vizinho_cima
                    else:
                        rotulo_atual = rotulo_atual + 1
                        resultado[x][y] = rotulo_atual
            else:
                if resultado[x][y] == 1:
                    vizinho_cima = resultado[x-1][y]
                    if vizinho_cima > 0:
                        vizinho_esquerda = resultado[x][y-1]
                        if vizinho_esquerda > 0 and vizinho_esquerda == vizinho_cima:
                            resultado[x][y] = vizinho_esquerda
                        elif vizinho_esquerda > 0 and vizinho_esquerda != vizinho_cima:
                            if vizinho_cima < vizinho_esquerda:
                                resultado[x][y] = vizinho_cima
                                resultado[x][y-1] = vizinho_cima
                                vizinho_do_vizinho = y-2
                                while vizinho_do_vizinho >= 0:
                                    if resultado[x][vizinho_do_vizinho] != 0:
                                        resultado[x][vizinho_do_vizinho] = vizinho_cima
                                        vizinho_do_vizinho = vizinho_do_vizinho - 1
                                    else:
                                        break
                            else:
                                resultado[x][y] = vizinho_esquerda
                                resultado[x-1][y] = vizinho_esquerda
                                vizinho_do_vizinho = x-2
                                while vizinho_do_vizinho >= 0:
                                    if resultado[vizinho_do_vizinho][y] != 0:
                                        resultado[vizinho_do_vizinho][y] = vizinho_esquerda
                                        vizinho_do_vizinho = vizinho_do_vizinho - 1
                                    else:
                                        break
                            rotulo_atual = rotulo_atual - 1
                        else:
                            resultado[x][y] = vizinho_cima
                    else:
                        vizinho_esquerda = resultado[x][y-1]
                        if vizinho_esquerda > 0:
                            resultado[x][y] = vizinho_esquerda
                        else:
                            rotulo_atual = rotulo_atual + 1
                            resultado[x][y] = rotulo_atual

    return resultado


if __name__ == "__main__":
    main()