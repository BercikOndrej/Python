from concurrent.futures import ThreadPoolExecutor
import threading

# Počítadlo volných pracovníků + executor
# Pokud bychom nepočítali volné pracovníky, tak nastane deadlock viz dokumentace ->
# počítáme pracovníky a pokud není, žadná volný, vypočítame si to sami
free_workers = None
lock = threading.Semaphore(1)
executor = None

def parrallel_fibonacci(n):
    global free_workers, executor, lock

    if (n <= 1):
        return n
    elif (free_workers != 0):
        lock.acquire()
        free_workers = free_workers - 1
        lock.release()
        x = parrallel_fibonacci(n - 1)
        future = executor.submit(parrallel_fibonacci, n - 2)
        y = future.result()
        lock.acquire()
        free_workers = free_workers + 1
        lock.release()
        return x + y
    else:
        return parrallel_fibonacci(n - 1) + parrallel_fibonacci(n -2)


def nth_parrallel_fibonacci(n, workers_count):
    global free_workers, lock, executor

    free_workers = workers_count
    executor = ThreadPoolExecutor(max_workers=workers_count)
    return parrallel_fibonacci(n)


# Main
print(nth_parrallel_fibonacci(37, 8))
executor.shutdown()