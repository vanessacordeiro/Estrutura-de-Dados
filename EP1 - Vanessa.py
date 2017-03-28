import random
from time import time

def main():
    dic = {2000: gerarVetor(2000),
           4000: gerarVetor(4000),
           6000: gerarVetor(6000),
           8000: gerarVetor(8000),
           10000: gerarVetor(10000),
           12000: gerarVetor(12000),
           14000: gerarVetor(14000),
           16000: gerarVetor(16000),
           18000: gerarVetor(18000),
           20000: gerarVetor(20000),
           22000: gerarVetor(22000)}

    global v
    x = 2000
    y = 0

    print('-' * 65,
          '\n|{:^11}|'.format(' '), '{:^50}|'.format('time(s)'),
          '\n' + '-' * 65,
          '\n|{:^11}|'.format('n'), '{:^11}|'.format('Mergesort'), '{:^11}|'.format('Quicksort'),
          '{:^11}|'.format('Selection'), '{:^11}|'.format('Native'))

    while x <=22000:
        temp = []
        v = dic[x]
        while y<4:
            temp.append(cronometra(y))
            y+=1

        print('|{:^11}|'.format(x),"{0:^11.2f}|".format(temp[0]),"{0:^11.2f}|".format(temp[1]),"{0:^11.2f}|".format(temp[2]),"{0:^11.2f}|".format(temp[3]))
        y = 0
        del(temp)
        x+=2000
    print('-' * 65)

#======= Gerador de Vetores ========
def gerarVetor(n):
    vetor = []
    vetor = list(range(0, n))
    random.shuffle(vetor)
    return vetor
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

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
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
def selection(v):
    resp = []
    while len(v) > 0:
        m = min(v)
        resp.append (m)
        v.remove(m)
    return resp
#===================================

#============ NATIVE ===============
def native(v):
    v.sort()
    return v
#===================================

#=========== CRONOMETRA ============
def cronometra(d):
    if d == 0:
        tempo = time()
        mergesort(v)
    elif d==1:
        tempo = time()
        quicksort(v)
    elif d==2:
        tempo = time()
        selection(v)
    elif d==3:
        tempo = time()
        native(v)
    return time()-tempo
#===================================

if __name__ == "__main__":
    main()
