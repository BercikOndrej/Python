from concurrent.futures import ThreadPoolExecutor
from random import randint
import threading


# Používám algoritmus, který jsem již napsal v rámci 2.úkolu do předmětu ZP4CS - ParallelMergeSort

# Zde si budu počítat, kolik vláken můžu zrovna využít -> pokud nebude žádné k dizpozici, provede to hlávní vlákno.
free_threads = None
lock = threading.Semaphore(1)
executor = None

# Funkce parallel_merge_sort -> funkce má navíc argument hloubka funkce
# Tu může nastavit uživatel a znamená, že od určité úrovně zanoření se nebudou používat vlákna
# To má za následek větší efektivitu, protože volat vlákno aby setřídilo seznam o jednom prvku nemá úplně smysl

# Startovací funkce, která mi provede inicializaci potřebných proměnných
def parallel_merge_sort(list, recursion_depth, threads_count):
    global free_threads, executor

    free_threads = threads_count
    executor = ThreadPoolExecutor(max_workers=threads_count)
    return true_parallel_merge_sort(list, recursion_depth)

def true_parallel_merge_sort(list, recursion_depth):
    global free_threads, executor, lock

    # Pokud není co rozdělit přastávám s rekurzí
    if(len(list) <= 1):
        return None

    # Rozdělím si pole
    center_index = int(len(list) / 2)
    left = list[:center_index]
    right = list[center_index:]

    # Pokud budeme v hloubce, kde máme povoleno pracovat s vlákny a máme nějaké k dizpozici, tak je použijeme
    if(recursion_depth > 0 and free_threads != 0):
        lock.acquire()
        free_threads -= 1
        lock.release()
        # Předám práci
        future = executor.submit(true_parallel_merge_sort, left, recursion_depth - 1)
        true_parallel_merge_sort(right, recursion_depth - 1)
        # Počkám až ji vykoná
        temp = future.result()
        # A uvolním vlákno
        lock.acquire()
        free_threads += 1
        lock.release()

    # Pokud nejsou dostupná vlákná, udělá to hlavní vlákno
    else:
        true_parallel_merge_sort(left, recursion_depth - 1)
        true_parallel_merge_sort(right, recursion_depth - 1)

    # Provedu slití polí
    merge(list, left, right)

def merge(list, left, right):
    left_index = 0
    right_index = 0

    # Sliju pole do vásledného listu
    while(left_index < len(left) and right_index < len(right)):
        if(left[left_index] < right[right_index]):
            list[left_index + right_index] = left[left_index]
            left_index += 1
        else:
            list[left_index + right_index] = right[right_index]
            right_index += 1

    # Pokud něco zbylo v levém poli, je to setřízené a tudíž to můžu nasypat do výsledného listu
    # analogicky pro pravé pole
    if(left_index < len(left)):
        while(left_index < len(left)):
            list[left_index + right_index] = left[left_index]
            left_index += 1
    else:
        while(right_index < len(right)):
            list[left_index + right_index] = right[right_index]
            right_index += 1


# Funkce pro vytvoření pole náhodných čísel o zadané velikosti a rozmezí
def random_int_array(length, start, end):
    array = []
    for i in range(length):
        array.append(randint(start, end))
    return array

# Main
list = random_int_array(30, 1, 150)
print( "Nesetřízené pole:\n" + str(list) + "\n")
# Zavolám funkci parallel_merge_sort na toto pole, budu používat 5 vláken pouze do hloubky 5
parallel_merge_sort(list, 4, 5)
print("Steřízené pole:\n" + str(list) + "\n")
executor.shutdown()