import threading
import time
import random

class SimpleSemaphore:
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

# Função que será executada pelas threads
def is_palindrome_stack(name, semaphore, result, arr):

    print(f"Thread {name} iniciada")

    results = []
    for s in arr:
        stack = list(s)
        reversed_s = ''
        while stack:
            reversed_s += stack.pop()
        results.append(s == reversed_s)
       
    print(f"Thread {name} terminou o problema palindromos")
    
    if semaphore.acquire():
        try:
            print(f"Thread {name} acessou a lista result")
            result.append(name)
        finally:
            print(f"Thread {name} liberou a lista result")
            semaphore.release()
    else:
        print(f"Thread {name} não conseguiu acessar a lista e gravar seu id")

# Número de threads que podem acessar o recurso simultaneamente
semaphore = SimpleSemaphore(1)

# Lista para armazenar o resultado
result = []

# Criar e iniciar as threads
threads = []
for i in range(2):
    t = threading.Thread(target=is_palindrome_stack, args=(i, semaphore, result, arr))
    threads.append(t)
    t.start()

# Aguardar todas as threads terminarem
for t in threads:
    t.join()

print("Todas as threads terminaram.")
print("Resultado:", result)