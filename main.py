import threading
import time
import random
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init


init(autoreset=True)


#Fibonacci 
class fibonacci():
    
    def __init__(self, method):
        self.method = method
        if self.method == 1:
            self.fibonacci_recursive(random.randint(15, 35))
        elif self.method == 2:
            self.fibonacci_iterative(random.randint(15, 35))
        else:
            raise ValueError("Fibonacci: método desconhecido")
        
    def fibonacci_recursive(self, n): #1
        if n <= 1:
            return True
        else:
            return self.fibonacci_recursive(n-1) + self.fibonacci_recursive(n-2)

    def fibonacci_iterative(self, n): #2
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a



#Ordenação
class sorting():
    def __init__(self, method):
        self.method = method
        if self.method == 1:
            self.bubble_sort(array)
        elif self.method == 2:
            self.insertion_sort(array)
        else:
            raise ValueError("Ordenação: método desconhecido")
        
    def bubble_sort(self, arr): #1
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def insertion_sort(self, arr): #2
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr



#Palindromos
class palindrome():
    def __init__(self, method):
        self.method = method
        if self.method == 1:
            self.is_palindrome_stack(words)
        elif self.method == 2:
            self.is_palindrome_deque(words)
        else:
            raise ValueError("Palíndromos: método desconhecido")
        
    def is_palindrome_stack(self, arr): #1
        results = []
        for s in arr:
            stack = list(s)
            reversed_s = ''
            while stack:
                reversed_s += stack.pop()
            results.append(s == reversed_s)
        return results

    def is_palindrome_deque(self, arr): #2
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



#Semaforo
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

class MyBarrier:
    def __init__(self, n):
        self.n = n
        self._count = 0
        self._condition = threading.Condition()

    def esperar(self):
        with self._condition:
            self._count += 1
            if self._count == self.n:
                self._count = 0  # Reset para reutilizar a barreira
                self._condition.notify_all()
            else:
                self._condition.wait()

#Função que cria as threads
def mythread(name, id):

    for i in range(10):
        task = random.choice(challenges)
        task(random.randint(1, 2))
        if semaphore.acquire():
            print(f"{Fore.GREEN}Thread {name} completou o desafio {task.__name__} e deu lock.")
            pontuacao[id] += 1
            time.sleep(random.uniform(0.2, 0.4))
            semaphore.release()
            print(f"{Fore.BLUE}Thread {name} completou o desafio {task.__name__} e deslockou.")
        else:
            print(f"{Fore.RED}Thread {name} terminou {task.__name__}  e não conseguiu lock no semáforo.")   
            time.sleep(random.uniform(0.4, 0.6))
        print(f"{Fore.YELLOW}Thread {name} chegou na barreira.")
        barreira.esperar()
        print(f"{Fore.CYAN}Thread {name} passou da barreira.")

#Lista de palavras utilizadas no desafio de palindromos
words = [
    "radar", "sistemas", "level", "rotor", "civic", "madam", "refer", "deified", "racecar", "repaper", "reviver",
    "redder", "stats", "tenet", "wow", "noon", "kayak", "malayalam", "solos", "minim", "madam", "python",
    "abba", "operacionais", "bob", "eve", "otto", "anna", "peep", "deed", "pop", "mum", "nun", "amor",
    "wow", "gig", "civic", "radar", "level", "rotor", "madam", "refer", "deified", "racecar", "programa",
    "repaper", "reviver", "redder", "stats", "tenet", "wow", "noon", "kayak", "malayalam", "solos", "robespierre"
]

#Lista de números utilizados no desafio de ordenação
array = [34, 7, 23, 32, 5, 62, 32, 2, 1, 4, 12, 22, 45, 33, 21, 56, 78, 
         90, 11, 13, 15, 17, 19, 20, 25, 27, 29, 31, 35, 37, 39, 41, 43, 
         47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79]

#Emojis de Pódio
medals = ["🥇", "🥈", "🥉", "😤","😤"]

#Array com as funções dos desafios	
challenges = [fibonacci, sorting, palindrome]

#Inicialização do semáforo
semaphore = MySemaphore(1)

#Inicialização da barreira
barreira = MyBarrier(5)

#Array com as pontuações dos jogadores
pontuacao = [0, 0, 0, 0, 0]

#Array com as threads
threads = []

#Criação das threads com ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    futures.append(executor.submit(mythread, "Player1", 0))
    futures.append(executor.submit(mythread, "Player2", 1))
    futures.append(executor.submit(mythread, "Player3", 2))
    futures.append(executor.submit(mythread, "Player4", 3))
    futures.append(executor.submit(mythread, "Player5", 4))


    for future in futures:
        future.result()
        
print("Todas as threads terminaram.")

print("Pontuação final:")

#Salvar pontuações junto aos seusn índices que identificam a thread que a fez
pontuacao_com_indices = [(pontuacao[i], i) for i in range(5)]

#Ordenar pontuações
pontuacao_ordenada = sorted(pontuacao_com_indices, key=lambda x: x[0], reverse=True)

#Imprimir pontuações
a = 0
for pontuacao, i in pontuacao_ordenada:
    print(medals[a], end=" ")
    print(f"Player {i + 1}: {pontuacao} pontos")
    a += 1