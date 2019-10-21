

def main():
    #========== Organiza Cavaleiros ==========
    arq = open(r'C:\Users\Vanessa\Desktop\FATEC\2019.2\ED\Estrutura-de-Dados\EP2\cavaleiros.txt')
    dic = split_nomes(arq)
    organiza_cavaleiros(dic)

    #============= Casa as Damas =============
    arq = open(r'C:\Users\Vanessa\Desktop\FATEC\2019.2\ED\Estrutura-de-Dados\EP2\casamento.txt')
    dic = split_nomes(arq)
    casa_as_damas(dic)


def organiza_cavaleiros(dic):
    cavaleiros = []
    for k in dic:
        cavaleiros.append(k)
        
    print('-'*71, '\n|{:^70}|\n'.format('Távola Redonda'),'-'*71)
    for sequencia in permutações(cavaleiros):
        if organiza_mesa(sequencia, dic) is True:
            print('| {}{:^62} |\n'.format("Mesa: ", " - ".join(sequencia)), '-'*71)
            return 0
    print('| {}{:^29} |\n'.format('Não é possível arrumar os 7 cavaleiros.', ' '), '-'*71)
    
def casa_as_damas(dic):
    damas = []
    for key in dic:
        damas.append(key)

    print('-'*71, '\n|{:^70}|\n'.format('Casando as Damas'),'-'*71)
    casais = []
    for s in enumerações(damas):
        lista = []
        for dama in s:
            lista.extend([i for i in dic[dama]])
        if(len(set(lista)) >= len(s)):
            continue
        else:
            print('| {}{:^43} |\n'.format('Casamento não é possível.', ' '), '-'*71)
            return 0
    print('| {}{:^47} |\n'.format('Casamento é possível.', ' '), '-'*71)

def split_nomes(arq):
    nomes = []
    
    for line in arq:
        linha = line.split('\n')
        nomes.append(linha[0].split())
    return organiza_preferencias(nomes)

def organiza_preferencias(listas):
    p = {}
    for l in listas:
        p.update({l[0]: l[1:]})
    return p

def organiza_mesa(sequencia, dic):   
    for i in range(len(sequencia)):
        if sequencia[i-1] not in dic[sequencia[i]]:
            return False
    return True
        

#========= Algoritmo de Merlin =========
def enumerações(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0: break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista

def combinações(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinações(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc
 
def permutações(items):
    return combinações(items, len(items))

 
if __name__ == "__main__":
    main()