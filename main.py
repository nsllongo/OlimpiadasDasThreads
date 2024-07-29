import threading 
import time
from collections import deque



#Fibonacci 
def fibonacci_recursive(n): #1
    if n <= 1:
        return n
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

semaphore = MySemaphore(1)

Player1 = threading.Thread(target=fibonacci_recursive, args=("Player1", semaphore, result), name="Player1")
Player2 = threading.Thread(target=fibonacci_iterative, args=("Player2", semaphore, result), name="Player2")

Player1.start()
Player2.start()

Player1.join
Player2.join

Player1 = threading.Thread(target=check_palindrome, args=("Player1", semaphore, result, is_palindrome_deque), name="Player1")
Player2 = threading.Thread(target=check_palindrome, args=("Player2", semaphore, result, is_palindrome_stack), name="Player2")

Player1.start()
Player2.start()

Player1.join
Player2.join


print("Todas as threads terminaram.")