import threading 
import time
from collections import deque

pontuacao = [0, 0, 0, 0]
threads = []

#Fibonacci 
def fibonacci_recursive(n): #1
    if n <= 1:
        return True
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n): #2
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a



#Ordenação
def bubble_sort(arr): #1
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr): #2
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



#Palindromos
def is_palindrome_stack(arr): #1
    results = []
    for s in arr:
        stack = list(s)
        reversed_s = ''
        while stack:
            reversed_s += stack.pop()
        results.append(s == reversed_s)
    return results

def is_palindrome_deque(arr): #2
    results = []
    for s in arr:
        d = deque(s)
        while len(d) > 1:
            if d.popleft() != d.pop():
                results.append(False)
                break
        else:
            results.append(True)
    return results

def check_palindrome(method):
    words = [
    "radar", "sistemas", "level", "rotor", "civic", "madam", "refer", "deified", "racecar", "repaper", "reviver",
    "redder", "stats", "tenet", "wow", "noon", "kayak", "malayalam", "solos", "minim", "madam", "python",
    "abba", "operacionais", "bob", "eve", "otto", "anna", "peep", "deed", "pop", "mum", "nun", "amor",
    "wow", "gig", "civic", "radar", "level", "rotor", "madam", "refer", "deified", "racecar", "programa",
    "repaper", "reviver", "redder", "stats", "tenet", "wow", "noon", "kayak", "malayalam", "solos", "robespierre"
]
    if method == 1:
        return is_palindrome_stack(words)
    elif method == 2:
        return is_palindrome_deque(words)
    else:
        raise ValueError("Palíndromos: método desconhecido")



class MySemaphore:
    def __init__(self, initial):
        self._lock = threading.Lock()
        self._counter = initial

    def acquire(self):
        with self._lock:
            if self._counter > 0:
                self._counter -= 1
                return True
            else:
                return False

    def release(self):
        with self._lock:
            self._counter += 1



def first_thread(nome):


    fibonacci_recursive(10)
    if semaphore.acquire():
        print(f"Thread {nome} terminou fibonacci recursivo e deu lock no semáforo.")
        pontuacao[0] += 1
        time.sleep(1)
        semaphore.release()
        print(f"Thread {nome} terminou fibonacci recursivo e deslockou o semáforo.")

    else:
        print(f"Thread {nome} terminou fibonacci recursivo e não conseguiu lock no semáforo.")   


    bubble_sort([3, 2, 1])
    if semaphore.acquire():
        print(f"Thread {nome} terminou bubble sort e deu lock no semáforo.")
        pontuacao[0] += 1
        time.sleep(1)
        semaphore.release()
        print(f"Thread {nome} terminou bubble sort e deslockou o semáforo.")

    else:
        print(f"Thread {nome} terminou bubble sort e não conseguiu lock no semáforo.")


    check_palindrome(1) #is_palindrome_stack
    if semaphore.acquire():
        print(f"Thread {nome} terminou palíndromos com stack e deu lock no semáforo.")
        pontuacao[0] += 1
        time.sleep(1)
        semaphore.release()
        print(f"Thread {nome} terminou palíndromos com stack e deslockou o semáforo.")
    else:
        print(f"Thread {nome} terminou palíndromos com stack e não conseguiu lock no semáforo.")


def second_thread(nome):


    fibonacci_recursive(10)
    if semaphore.acquire():
        print(f"Thread {nome} terminou fibonacci recursivo e deu lock no semáforo.")
        pontuacao[1] += 1
        time.sleep(1)
        semaphore.release()
        print(f"Thread {nome} terminou fibonacci recursivo e deslockou o semáforo.")

    else:
        print(f"Thread {nome} terminou fibonacci recursivo e não conseguiu lock no semáforo.")   


    bubble_sort([3, 2, 1])
    if semaphore.acquire():
        print(f"Thread {nome} terminou bubble sort e deu lock no semáforo.")
        pontuacao[1] += 1
        time.sleep(1)
        semaphore.release()
        print(f"Thread {nome} terminou bubble sort e deslockou o semáforo.")

    else:
        print(f"Thread {nome} terminou bubble sort e não conseguiu lock no semáforo.")


    check_palindrome(2) #is_palindrome_deque
    if semaphore.acquire():
        print(f"Thread {nome} terminou palíndromos com deque e deu lock no semáforo.")
        pontuacao[1] += 1
        time.sleep(1)
        semaphore.release()
        print(f"Thread {nome} terminou palíndromos com deque e deslockou o semáforo.")
    else:
        print(f"Thread {nome} terminou palíndromos com deque e não conseguiu lock no semáforo.")


def third_thread(nome):
    
        fibonacci_iterative(20)
        if semaphore.acquire():
            print(f"Thread {nome} terminou fibonacci iterativo e deu lock no semáforo.")
            pontuacao[2] += 1
            time.sleep(1)
            semaphore.release()
            print(f"Thread {nome} terminou fibonacci iterativo e deslockou o semáforo.")
    
        else:
            print(f"Thread {nome} terminou fibonacci iterativo e não conseguiu lock no semáforo.")   
    
    
        insertion_sort([3, 2, 1])
        if semaphore.acquire():
            print(f"Thread {nome} terminou insertion sort e deu lock no semáforo.")
            pontuacao[2] += 1
            time.sleep(1)
            semaphore.release()
            print(f"Thread {nome} terminou insertion sort e deslockou o semáforo.")
    
        else:
            print(f"Thread {nome} terminou insertion sort e não conseguiu lock no semáforo.")
    
    
        check_palindrome(1) #is_palindrome_stack
        if semaphore.acquire():
            print(f"Thread {nome} terminou palíndromos com stack e deu lock no semáforo.")
            pontuacao[2] += 1
            time.sleep(1)
            semaphore.release()
            print(f"Thread {nome} terminou palíndromos com stack e deslockou o semáforo.")
        else:
            print(f"Thread {nome} terminou palíndromos com stack e não conseguiu lock no semáforo.")


def fourth_thread(nome):
        

        fibonacci_iterative(20)
        if semaphore.acquire():
            print(f"Thread {nome} terminou fibonacci iterativo e deu lock no semáforo.")
            pontuacao[3] += 1
            time.sleep(1)
            semaphore.release()
            print(f"Thread {nome} terminou fibonacci iterativo e deslockou o semáforo.")
    
        else:
            print(f"Thread {nome} terminou fibonacci iterativo e não conseguiu lock no semáforo.")   
        
        
        bubble_sort([3, 2, 1])
        if semaphore.acquire():
            print(f"Thread {nome} terminou bubble sort e deu lock no semáforo.")
            pontuacao[3] += 1
            time.sleep(1)
            semaphore.release()
            print(f"Thread {nome} terminou bubble sort e deslockou o semáforo.")

        else:
            print(f"Thread {nome} terminou bubble sort e não conseguiu lock no semáforo.")


        check_palindrome(2) #is_palindrome_deque
        if semaphore.acquire():
            print(f"Thread {nome} terminou palíndromos com deque e deu lock no semáforo.")
            pontuacao[3] += 1
            time.sleep(1)
            semaphore.release()
            print(f"Thread {nome} terminou palíndromos com deque e deslockou o semáforo.")
        else:
            print(f"Thread {nome} terminou palíndromos com deque e não conseguiu lock no semáforo.")






semaphore = MySemaphore(3)
pontuacao = [0, 0, 0, 0]
threads = []

threads.append(threading.Thread(target=first_thread, args=("Player1",)))
threads.append(threading.Thread(target=second_thread, args=("Player2",)))
threads.append(threading.Thread(target=third_thread, args=("Player3",)))
threads.append(threading.Thread(target=fourth_thread, args=("Player4",)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Todas as threads terminaram.")

print("Pontuação final:")
for i in pontuacao:
    print(f"Player {i}: {pontuacao[i]}")