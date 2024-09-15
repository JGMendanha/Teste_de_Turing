import socket, sys
from threading import Thread
import api
from time import sleep

HOST = '127.0.0.1' 
PORT = 20000        
BUFFER_SIZE = 1024  

def on_new_client(clientsocket, addr, timer, option):
    info_client = clientsocket.recv(BUFFER_SIZE).decode('utf-8')
    questions = []
    answers = []
    test_turing = []
    turing = []
    hits = 0
    
    while True:
        try:
            data = clientsocket.recv(BUFFER_SIZE)
            if not data:
                break
            text_received = data.decode('utf-8')

            if text_received == 'bye':
                with open("registros.txt", 'a') as file:
                    file.write("=======================================================================================================================\n")
                    file.write(f"NOME DO CLIENTE: {info_client}\n")
                    for i in range(len(questions)):
                        if test_turing[i] == turing[i]:
                            hit = "SIM"
                        else:
                            hit = "NAO"
                        file.write("-------------------------------------------------------------------------------------------------------------------\n")
                        file.write(f"PERGUNTA: {questions[i]}\nRESPOSTA: {answers[i]}\nRESPOSTA DO TESTE DE TURING: {test_turing[i]}\nQUEM RESPONDEU: {turing[i]}\nACERTOU QUEM RESPONDEU ?: {hit}\n")
                    file.write("=======================================================================================================================\n")
                
                for j in range(len(test_turing)):
                    if turing[j] == test_turing[j]:
                        hits += 1
                
                with open("ranking.txt", 'a') as file2:
                    size_questions = len(questions)
                    percent = (hits / size_questions) * 100
                    file2.write(f"{info_client}:{percent:.2f}\n")
                
                ordenar_por_percentual()

                print("=======================================================================================================================\n")
                print(f"O CLIENTE {info_client} ENCERROU A CONEXÃO\n")
                print("=======================================================================================================================\n")
                clientsocket.close()
                return
                
            questions.append(text_received)
            print("\n======================================================================================================================\n")
            
            if option == 1: 
                print(f"PERGUNTA DO CLIENTE: {text_received}")
                answer = api.question(text_received)
                print(f"RESPOSTA DO CHAT GPT: {answer}")
                turing.append("maquina")
            else: 
                print(f"PERGUNTA DO CLIENTE: {text_received}")
                who_answer = int(input("QUEM DEVE RESPONDER ESSA PERGUNTA? (1 PARA HUMANO / 2 PARA MÁQUINA) "))
                if who_answer == 1:
                    answer = str(input("DIGITE A RESPOSTA: "))
                    turing.append("humano")
                else:
                    answer = api.question(text_received)
                    print(f"RESPOSTA DO CHAT GPT: {answer}")
                    turing.append("maquina")

            answers.append(answer)

            sleep(timer)

            clientsocket.send(answer.encode()) 

            test = clientsocket.recv(BUFFER_SIZE).decode('utf-8')
            test_turing.append(test)

        except Exception as error:
            print("CONEXÃO PERDIDA\nTENTE NOVAMENTE")
            return

def ordenar_por_percentual():
    with open("ranking.txt", "r") as file:
        linhas = file.readlines()

    rank = []
    for linha in linhas:
        name, percent = linha.strip().split(":")
        rank.append((name, float(percent))) 

    sort = sorted(rank, key=lambda x: x[1], reverse=True)

    with open("ranking.txt", "w") as file:
        for name, percent in sort:
            file.write(f"{name}:{percent:.2f}\n")

def main(args):
    option = int(input("BEM VINDO À APLICAÇÃO DO LADO SERVIDOR\nPARA COMEÇAR, DIGA QUAL MODO DESEJA EXECUTAR\nDIGITE 1 PARA MODO AUTOMÁTICO E 2 PARA MODO CONTROLADO: "))
    timer = int(input("DIGITE O TEMPO EM SEGUNDOS QUE A APLICAÇÃO DEVE ESPERAR PARA ENVIAR A RESPOSTA AO CLIENTE: "))
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            print("Servidor iniciado")
            while True:
                server_socket.listen()
                clientsocket, addr = server_socket.accept()
                print('Conectado ao cliente no endereço:', addr)
                t = Thread(target=on_new_client, args=(clientsocket, addr, timer, option))
                t.start()
                
    except Exception as error:
        print("Erro na execução do servidor!!")
        print(error)

if __name__ == "__main__":
    main(sys.argv[1:])
