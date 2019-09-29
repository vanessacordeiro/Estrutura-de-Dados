import random
from time import time

def main():
    dic = {5000: gerarVetor(5000),
           10000: gerarVetor(10000),
           15000: gerarVetor(15000),
           20000: gerarVetor(20000),
           25000: gerarVetor(25000)}

    dic_ordenado = {}
    x = 5000
    y = 0

    print('-' * 56, '[EP1 - Vale a pena ordenar?]', '-' * 57,
          '\n|{:^141}|\n|{:^141}|'.format('FATEC São José dos Campos    Matéria: Estrutura de Dados', 'Aluno(s): Thiago Luiz e Vanessa Cordeiro'),
          '\n' + '-' * 143,
          '\n|{:^11}|'.format(' '), '{:^63}|'.format('Tempos de Ordenação'), '{:^63}|'.format('Número de buscas'),
          '\n' + '-' * 143,
          '\n|{:^11}|'.format('n'), '{:^11}|'.format('Mergesort'), '{:^11}|'.format('Quicksort'),
          '{:^11}|'.format('Selection'), '{:^11}|'.format('Insert'), '{:^11}|'.format('Native'),
          '{:^11}|'.format('Mergesort'), '{:^11}|'.format('Quicksort'),
          '{:^11}|'.format('Selection'), '{:^11}|'.format('Insert'), '{:^11}|'.format('Native'))

    while x <=20000:
        temp = []
        buscas = []
        numero = num_random(dic[x])
        while y<5:
            lista = dic[x].copy()
            tempo, dic_ordenado = cronometra(x, y, lista, dic_ordenado)
            temp.append(tempo)
            y= y + 1
        y = 0

        while y<5:
            buscas.append(num_buscas(numero, dic_ordenado[x], dic[x], temp[y]))
            y= y + 1

        
        print('|{:^11}|'.format(x),"{0:^11.2f}|".format(temp[0]),"{0:^11.2f}|".format(temp[1]),"{0:^11.2f}|".format(temp[2]),"{0:^11.2f}|".format(temp[3]), "{0:^11.2f}|".format(temp[4]),
        '{:^11}|'.format(buscas[0]), '{:^11}|'.format(buscas[1]), '{:^11}|'.format(buscas[2]), '{:^11}|'.format(buscas[3]), '{:^11}|'.format(buscas[4]))
        y = 0
        del(buscas)
        del(temp)
        x+=5000
    print('-' * 143)

#======= Gerador de Vetores ========
def gerarVetor(n):
    vetor = []
    vetor = list(range(0, n))
    random.shuffle(vetor)
    return vetor
#===================================

#========= NÚMERO RANDOM ===========
def num_random(lista):
    return random.choice(lista)
#===================================

#============ MERGESORT ============
def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    else:
        m = len(lista) // 2
        e = mergesort(lista[:m])
        d = mergesort(lista[m:])
        return merge(e, d)
#===================================

#============ QUICKSORT ============
def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    iguais  = [x for x in lista if x == pivo]
    menores = [x for x in lista if x < pivo]
    maiores = [x for x in lista if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)
#===================================

#============ SELECTION ============
def selection(lista):
    resp = []
    while len(lista) > 0:
        m = min(lista)
        resp.append (m)
        lista.remove(m)
    return resp
#===================================

#============ NATIVE ===============
def native(lista):
    lista.sort()
    return lista
#===================================

#============= INSERT ==============
def insert(lista):
    for j in range(1, len(lista)):
        x = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > x:
            lista[i + 1] = lista[i]
            i = i - 1
        lista[i + 1] = x
    return lista
#===================================

#======== BUSCA SEQUENCIAL =========
def busca_sequencial(x, lista):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return i
#===================================

#========== BUSCA BINARIA ==========
def busca_binaria(lista, x, esq, dir, tentativa):
	meio = (esq + dir) // 2
	aux_num = lista[meio]
	if x == aux_num:
		return tentativa
	elif x > aux_num:
		return busca_binaria(lista, x, meio, dir, tentativa + 1)
	return busca_binaria(lista, x, esq, meio, tentativa + 1)
#===================================

#=========== CRONOMETRA ============
def cronometra(key, d, lista, dic_ordenado):
    if d == 0:
        tempo = time()
        mergesort(lista)
    elif d==1:
        tempo = time()
        quicksort(lista)
    elif d==2:
        tempo = time()
        selection(lista)
    elif d==3:
        tempo = time()
        insert(lista)
    elif d==4:
        tempo = time()
        dic_ordenado[key] = native(lista)
    
    return time()-tempo, dic_ordenado
#===================================

#========= CONTA AS BUSCAS =========
def num_buscas(num, dic_ordenado, dic, tempo_ordenacao):
    tempo = time()
    cont = 0
    while True:
        cont = cont + 1
        buscas_binarias = busca_binaria(dic_ordenado, num, 0, len(dic_ordenado), 1)
        buscas_sequenciais = busca_sequencial(num, dic)
        t = (time() - tempo)
        if tempo_ordenacao<= t:
            break

    return cont

if __name__ == "__main__":
    main()
