import random
import time

def insertion_sort(L):
    for j in range(len(L)):
        key = L[j]
        i = j -1
        while i >= 0 and key < L[i]:
            L[i + 1] = L[i]
            i = i - 1
        L[i + 1] = key
        fin = time.time()
    return L

n = 50000
L = list(range(n))
random.shuffle(L)
inicio = time.time()
insertion_sort(L)
final = time.time()
print("Tiempo inicial: ", inicio)
print("Tiempo final: ", final)
print("Tiempo total: ", final - inicio)