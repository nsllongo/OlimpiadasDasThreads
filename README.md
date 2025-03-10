Este projeto foi realizado pelo aluno Lucas Longo R. De Souza para contemplar a avaliação da matéria MATA58-SISTEMAS OPERACIONAIS ministrada pelo Prof. Robespierre Pitta, na Universidade Federal da Bahia.

O jogo consiste em uma competição, onde os players são threads diferentes que objetivam resolver desafios matemáticos com algoritimos diferentes, dentre os desafios temos: fibonacci, ordenação de arrays e verificação de palíndromos.

Lógica da pontuação:

    Cada thread corresponde a um indice na array pontuação, por exemplo, a thread 1 é o índice 0 na array, assim,
    a thread passa um argumento para a sua função que permite que ela apenas incremente mais pontos no índice 0 da
    array, quando o programa termina, criamos uma tupla que salva o índice e a pontuação, posteriormente essa tupla
    é ordenada para que os players com mais pontos fiquem a cima, criando um pódio.

    
Blibiotecas:

    Threading
    Utilizando a blibioteca threading, usei a função de lock para implementar um simples semáforo que é utilizado 
    no jogo, onde toda vez que uma thread termina um desafio, a mesma usa o semaforo para ter acesso a uma array 
    onde incrementa sua própia pontuação, assim, se outras threads terminarem logo em seguida e tentarem incrementar
    suas respectivas pontuações, elas serão impedidas e seguirão para o proximo desafio.

    Colorama:
    utilizada para mudar a cor do log no terminal.

    Time:
    utilizada para proporcionar intervalos atraves do método sleep.

    Random: que proporciona variação nos desafios, permitindo que cada rodada seja diferente. Collections: para usar o método deque de verificação de palíndromos.

    Current.future: que disponibiliza o ThreadPoolExecutor, que faz as threads iniciarem de maneira simultânea.


Tutorial de execução:

    Tendo o Python 3.12(ou superior) instalado na sua máquina, basta copiar o repositório e executar através 
    da sua IDE de preferência. Lembre-se que blibiotecas como a colorama precisam ser instaladas, através do 
    comando "pip install colorama".
