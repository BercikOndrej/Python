import threading

# V iniciaci musíme určit kolik bude židlí v čekárně
CHAIRS_COUNT = 5

# Poté musíme zajistit aby kontroloval čekárnu právě jeden proces -> zamek chairs_mutex
free_chairs = CHAIRS_COUNT
chairs_mutex = threading.Semaphore(1)

# Na židli holiče vždy sedí pouze jeden zákazník
barber_chair = threading.Semaphore(1)

# Poté musíme dát najevo nějak holiči zda jsou zákazníci či nikoliv
customers = threading.Semaphore(0)

# Vlákno pro zákazníka
def get_hair_cut(customer_number):
    global free_chairs, chairs_mutex, barber_chair, customers

    chairs_mutex.acquire()
    if(free_chairs == 0):
        chairs_mutex.release()
        # Pokud není ani jedna volná židle. Zákazník odchází -> vlákno by mělo skončit
        return
    else:
        # Pokud ne posadí se na volnou židli a čeká až se uvolní barberova židle
        free_chairs = free_chairs - 1
        chairs_mutex.release()
        # Dá vědět holiči, že je připraven se nechat ostříhat
        customers.release()
        barber_chair.acquire()
        print("Customer number {} is going to be served.".format(customer_number))

#  Vlákno pro barbera
def cut_hair():
    global free_chairs, chairs_mutex, barber_chair, customers

    # Barber maká pořád -> spát může na začátku cyklu while -> tedy pokud customers budou na nule
    while(True):
        # Zde může spát pokud nebude zákazník.
        customers.acquire()
        # Jakmile se příjde zákazník, vezme jej na barberovi židli a uvolní místo v čekárně
        chairs_mutex.acquire()
        free_chairs = free_chairs + 1
        chairs_mutex.release()
        # Tady provede sestřih zákazníka
        print("Working")
        # A pote si vezme peníze, pošleho domů a uvolní barber židli
        print("Customer has been served.")
        barber_chair.release()

    # Takto holič pracuje pořád dokola, než mu skončí pracovní doba
    # Pokud nebude mít zákazníka -> u kroku customers.acquire() se zastaví a zdřímne si
    # Zákazník ho probudí krokem customers.release()

# Main

barber = threading.Thread(target=cut_hair)
barber.start()

# Holič bude mít za den bude mít návštěvu 7 zákazníků.
for i in range(7):
    customer = threading.Thread(target=get_hair_cut, args=(i,))
    customer.start()