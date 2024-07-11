import threading
from random import randint

buffer = []
size = 3
# Space nám říká, kolik je místa, kolik prvků můžeme přidat
space = threading.Semaphore(size)
lock = threading.Semaphore(1)
# Item ma 0 jelikož buffer je ze začátku prázdná -> má 0 prvků
item = threading.Semaphore(0)

def produce():
    global buffer, space, lock, item

    for i in range(3):
        space.acquire()
        lock.acquire()
        value = randint(0, 10)
        buffer.append(value)
        lock.release()
        print("Byl vyprodukovan prvek " + str(value) +".\n")
        item.release()

def consume():
    global buffer, lock, item, space

    for i in range(3):
        item.acquire()
        lock.acquire()
        print("Byl spotrebovan prvek " + str(buffer.pop()) + ".\n")
        lock.release()
        space.release()

# Main
p1 = threading.Thread(target=produce)
p2 = threading.Thread(target=produce)
p3 = threading.Thread(target=produce)
c1 = threading.Thread(target=consume)
c2 = threading.Thread(target=consume)
c3 = threading.Thread(target=consume)

p1.start()
p2.start()
p3.start()
c1.start()
c2.start()
c3.start()